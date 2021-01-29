# Neural networks
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-6/README.md
# Faces data from: http://conradsanderson.id.au/lfwcrop/

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
import tensorflow as tf
from tensorflow import keras
import h5py
import cv2
from pathlib import Path


class SmileNeuralNetwork:
    """
    Neural network class for detecting smiles.

    # 'Normal'
    # Train Loss:, 11.98
    # Train Accuracy: 95.34
    # ---------------------------------------
    # Test Loss:, 29.22
    # Test Accuracy: 89.30

    # 'Deep'
    # Train Loss:, 16.73
    # Train Accuracy: 93.14
    # ---------------------------------------
    # Test Loss:, 26.86
    # Test Accuracy: 89.05

    # 'Saved Deep'
    # Train Loss:, 21.65
    # Train Accuracy: 91.39
    # ---------------------------------------
    # Test Loss:, 19.27
    # Test Accuracy: 92.04

    Attributes
    ----------
    model : Model
    X_train : ndarray containing train data
    y_train : array containing train output labels
    X_test : ndarray containing test data
    y_test : array containing test output labels

    Methods
    -------
    __get_classified_images(self, file_path, class_value):
        Prepares classified images from the provided file.
    __prepare_data(self):
        Loads data, preprocesses it and splits it to train and test sets.
    __prepare_callbacks(self, name_part):
        Prepares callbacks which are going to be passed to the trained model.
    load_model(self, choice):
        Picks which neural network structure to load from the existing file and evaluates it.
    train_model(self, choice):
        Picks which neural network structure to train and evaluates it.
    __prepare_neural_network_model(self):
        Prepares model, creates layers.
    __prepare_deep_neural_network_model(self):
        Prepares model, creates layers.
    __compile_fit(self, callbacks):
        Compiles and trains the model.
    __evaluate(self):
        Evaluates model - prints loss and accuracy values for train and test sets.
    validate_with_camera(self):
        Runs camera, detects and marks face with a rectangle, displays whether person is smiling or not.
    """

    def __init__(self):
        """
        Creates initial model attribute and executes prepare data method.
        """
        self.model = None
        self.__prepare_data()

    def __get_classified_images(self, file_path, class_value):
        """
        Prepares classified images from the provided file.

        Parameters
        ----------
        file_path : str
        class_value : int (0 - not smiling, 1 - smiling)

        Returns
        -------
        X, y : arrays containing images data and labels
        """
        X = []
        y = []
        with open(file_path, 'r') as fp:
            while True:
                file_name = fp.readline()
                if not file_name:
                    break
                full_file_path = "./data/smile/faces/" + file_name.strip()
                if Path(full_file_path):
                    image = cv2.imread(full_file_path)
                    if image is not None:
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        X.append(image)
                        y.append(class_value)
        return X, y

    def __prepare_data(self):
        """
        Loads data, preprocesses it and splits it to train and test sets.

        Returns
        -------
        None
        """
        X_smiling, y_smiling = self.__get_classified_images('./data/smile/our-smile-list.txt', 1)
        X_not_smiling, y_not_smiling = self.__get_classified_images('./data/smile/our-non-smile-list.txt', 0)
        X = X_smiling + X_not_smiling
        y = y_smiling + y_not_smiling

        # Join a sequence of arrays along a new axis (stack method).
        X = np.stack(X)
        y = np.stack(y)
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3)
        self.X_train = self.X_train / 255
        self.X_test = self.X_test / 255

    def __prepare_callbacks(self, name_part):
        """
        Prepares callbacks which are going to be passed to the trained model.

        From: https://keras.io/api/callbacks/
        A callback is an object that can perform actions at various stages of training (e.g. at the start or end of an epoch, 
        before or after a single batch, etc).

        Parameters
        ----------
        name_part : str

        Returns
        -------
        callbacks : 1d array
        """
        callbacks = []
        early_stopping = keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=3,
            verbose=1)
        callbacks.append(early_stopping)
        model_checkpoint = keras.callbacks.ModelCheckpoint(
            filepath='./data/saved-models/smile' + name_part + '.hdf5',
            save_weights_only=False,
            monitor='val_loss',
            mode='min',
            save_best_only=True)
        callbacks.append(model_checkpoint)
        return callbacks

    def load_model(self, choice):
        """
        Picks which neural network structure to load from the existing file and evaluates it.

        Parameters
        ----------
        choice : int

        Returns
        -------
        None
        """
        default = './data/saved-models/smile'
        if choice == 1:
            path = default + '.hdf5'
        elif choice == 2:
            path = default + '-deep.hdf5'
        self.model = keras.models.load_model(path)
        self.__evaluate()

    def train_model(self, choice):
        """
        Picks which neural network structure to train and evaluates it.

        Parameters
        ----------
        choice : int

        Returns
        -------
        None
        """
        name_part = ''
        if choice == 1:
            self.__prepare_neural_network_model()
        elif choice == 2:
            self.__prepare_deep_neural_network_model()
            name_part = '-deep'
        callbacks = self.__prepare_callbacks(name_part)
        self.__compile_fit(callbacks)
        self.__evaluate()

    def __prepare_neural_network_model(self):
        """
        Prepares model, creates layers.

        Returns
        -------
        None
        """
        # Sequential model is a linear stack of layers
        self.model = keras.models.Sequential()
        # First parameter - number of output filters, second kernel size (1, 1), (3, 3), (5, 5), (7, 7) - value depends on the size of the images
        self.model.add(keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(64, 64, 3)))
        # Max pooling is  used to reduce the spatial dimensions of the output volume
        self.model.add(keras.layers.MaxPooling2D((2, 2)))
        self.model.add(keras.layers.Conv2D(32, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))
        self.model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))
        self.model.add(keras.layers.Flatten())
        # Dense layers - fully connected layers
        self.model.add(keras.layers.Dense(64, activation='relu'))
        self.model.add(keras.layers.Dense(1, activation='sigmoid'))

    def __prepare_deep_neural_network_model(self):
        """
        Prepares model, creates layers.

        Returns
        -------
        None
        """
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(64, 64, 3)))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))
        self.model.add(keras.layers.Conv2D(32, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))
        self.model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))
        self.model.add(keras.layers.Flatten())
        self.model.add(keras.layers.Dense(128, activation='relu'))
        self.model.add(keras.layers.Dense(86, activation='relu'))
        self.model.add(keras.layers.Dense(1, activation='sigmoid'))

    def __compile_fit(self, callbacks):
        """
        Compiles and trains the model.

        Parameters
        ----------
        callbacks - 1d array containing possible model callbacks

        Returns
        -------
        None
        """
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        # Trains the model
        self.model.fit(self.X_train, self.y_train, validation_data=(self.X_test, self.y_test), epochs=100, callbacks=callbacks)

    def __evaluate(self):
        """
        Evaluates model - prints loss and accuracy values for train and test sets.

        Returns
        -------
        None
        """
        print('Evaluating smile neural network...')
        loss, accuracy = self.model.evaluate(self.X_train, self.y_train) # Evaluates trained model
        print('Train Loss:, %.2f' % (loss*100))
        print('Train Accuracy: %.2f' % (accuracy*100))
        print('---------------------------------------')
        loss_test, accuracy_test = self.model.evaluate(self.X_test, self.y_test)
        print('Test Loss:, %.2f' % (loss_test*100))
        print('Test Accuracy: %.2f' % (accuracy_test*100))

    def validate_with_camera(self):
        """
        Runs camera, detects and marks face with a rectangle, displays whether person is smiling or not.

        Based on: https://realpython.com/face-detection-in-python-using-a-webcam/

        Haar Cascade classifier is an effective object detection approach which was proposed by Paul Viola and Michael Jones in their paper, 
        “Rapid Object Detection using a Boosted Cascade of Simple Features” in 2001.

        Returns
        -------
        None
        """
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        video_capture = cv2.VideoCapture(0)
        predict = 0
        while True:
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detects faces
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=10,
                minSize=(64, 64),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            for (x, y, w, h) in faces:
                xoffset = 20
                yoffset = 10
                cv2.rectangle(frame, (x+xoffset, y+yoffset), (x+w-xoffset, y+h-yoffset), (0, 255, 0), 2)
                fragment = frame[y+yoffset+5: y+h-yoffset-5, x+xoffset+5:x+w-xoffset-5]
                cv2.imwrite('./data/smile/camera.png', fragment)
                img = cv2.imread('./data/smile/camera.png')
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = cv2.resize(img, (64, 64))
                img = img.reshape(-1, 64, 64, 3) / 255
                predict = self.model.predict(img)
                print(predict)
                predict = (predict[0] > 0.5).astype("int32")

            font = cv2.FONT_HERSHEY_SIMPLEX
            if predict == 0:
                output = ":("
                bgr = (0, 0, 255)
            else:
                output = ":)"
                bgr = (0, 255, 0)
            cv2.putText(frame, output, (20, 50), font, 1, bgr, 3)
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()
