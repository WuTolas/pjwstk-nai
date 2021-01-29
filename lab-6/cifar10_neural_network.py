# Neural networks
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-6/README.md
# Based on: https://www.tensorflow.org/tutorials/images/cnn

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
import tensorflow as tf
from tensorflow import keras


class Cifar10NeuralNetwork():
    """
    Neural network class for animals classification.

    # 'Normal'
    # Train Loss:, 55.98
    # Train Accuracy: 80.45
    # ---------------------------------------
    # Test Loss:, 98.38
    # Test Accuracy: 67.81

    # 'Deep'
    # Train Loss:, 58.79
    # Train Accuracy: 79.30
    # ---------------------------------------
    # Test Loss:, 95.76
    # Test Accuracy: 68.61

    Attributes
    ----------
    model : Model
    X_train : ndarray containing train data
    y_train : ndarray containing train output labels
    X_test : ndarray containing test data
    y_test : ndarray containing test output labels

    Methods
    -------
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
    """

    def __init__(self):
        """
        Creates initial model attribute and executes prepare data method.
        """
        self.model = None
        self.__prepare_data()

    def __prepare_data(self):
        """
        Loads data, preprocesses it and splits it to train and test sets.

        Returns
        -------
        None
        """
        (self.X_train, self.Y_train), (self.X_test, self.Y_test) = keras.datasets.cifar10.load_data()
        X = np.concatenate((self.X_train,self.X_test))
        y = np.concatenate((self.Y_train,self.Y_test))
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3)
        self.X_train = self.X_train / 255
        self.X_test = self.X_test / 255

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
        default = './data/saved-models/cifar-10'
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
            filepath='./data/saved-models/cifar-10' + name_part + '.hdf5',
            save_weights_only=False,
            monitor='val_loss',
            mode='min',
            save_best_only=True)
        callbacks.append(model_checkpoint)
        return callbacks

    def __prepare_neural_network_model(self):
        """
        Prepares model, creates layers.

        Returns
        -------
        None
        """
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))
        self.model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))
        self.model.add(keras.layers.Flatten())
        self.model.add(keras.layers.Dense(64, activation='relu'))
        self.model.add(keras.layers.Dense(10, activation='softmax'))

    def __prepare_deep_neural_network_model(self):
        """
        Prepares model, creates layers.

        Returns
        -------
        None
        """
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))
        self.model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))
        self.model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))
        self.model.add(keras.layers.Flatten())
        self.model.add(keras.layers.Dense(64, activation='relu'))
        self.model.add(keras.layers.Dense(48, activation='relu'))
        self.model.add(keras.layers.Dense(10, activation='softmax'))

    def __compile_fit(self, callbacks):
        """
        Compiles and trains the model.

        Returns
        -------
        None
        """
        self.model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['sparse_categorical_accuracy'])
        self.model.fit(self.X_train, self.y_train, validation_data=(self.X_test, self.y_test),  epochs=32, callbacks=callbacks)

    def __evaluate(self):
        """
        Evaluates model - prints loss and accuracy values for train and test sets.

        Returns
        -------
        None
        """
        print('Evaluating cifar10 neural network...')
        loss, accuracy = self.model.evaluate(self.X_train, self.y_train)
        print('Train Loss:, %.2f' % (loss*100))
        print('Train Accuracy: %.2f' % (accuracy*100))
        print('---------------------------------------')
        loss_test, accuracy_test = self.model.evaluate(self.X_test, self.y_test)
        print('Test Loss:, %.2f' % (loss_test*100))
        print('Test Accuracy: %.2f' % (accuracy_test*100))
