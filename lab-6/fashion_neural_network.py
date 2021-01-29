# Neural networks
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-6/README.md
# Based on: https://www.tensorflow.org/tutorials/keras/classification

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
import tensorflow as tf
from tensorflow import keras


class FashionNeuralNetwork():
    """
    Neural network class for clothes classification.

    # 'Normal'
    # Train Loss:, 14.83
    # Train Accuracy: 94.66
    # ---------------------------------------
    # Test Loss:, 35.55
    # Test Accuracy: 89.08

    # 'Deep'
    # Train Loss:, 29.06
    # Train Accuracy: 89.07
    # ---------------------------------------
    # Test Loss:, 36.32
    # Test Accuracy: 86.82

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
        (self.X_train, self.Y_train), (self.X_test, self.Y_test) = keras.datasets.fashion_mnist.load_data()
        X = np.concatenate((self.X_train,self.X_test))
        y = np.concatenate((self.Y_train,self.Y_test))
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3)
        self.X_train = self.X_train.reshape(len(self.X_train), 784).astype("float32") / 255
        self.X_test = self.X_test.reshape(len(self.X_test), 784).astype("float32") / 255
        self.y_train = self.y_train.astype("float32")   
        self.y_test = self.y_test.astype("float32")

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
        if choice == 1:
            self.__prepare_neural_network_model()
        elif choice == 2:
            self.__prepare_deep_neural_network_model()
        self.__compile_fit()
        self.__evaluate()

    def __prepare_neural_network_model(self):
        """
        Prepares model, creates layers.

        Returns
        -------
        None
        """
        self.model = keras.models.Sequential()
        self.model.add(keras.Input(shape=(784,)))
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
        self.model.add(keras.Input(shape=(784,)))
        self.model.add(keras.layers.Dense(64, activation='relu'))
        self.model.add(keras.layers.Dense(32, activation='relu'))
        self.model.add(keras.layers.Dense(18, activation='relu'))
        self.model.add(keras.layers.Dense(10, activation='softmax'))

    def __compile_fit(self):
        """
        Compiles and trains the model.

        Returns
        -------
        None
        """
        self.model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['sparse_categorical_accuracy'])
        self.model.fit(self.X_train, self.y_train, epochs=50, batch_size=128)

    def __evaluate(self):
        """
        Evaluates model - prints loss and accuracy values for train and test sets.

        Returns
        -------
        None
        """
        print('Evaluating fashion neural network...')
        loss, accuracy = self.model.evaluate(self.X_train, self.y_train)
        print('Train Loss:, %.2f' % (loss*100))
        print('Train Accuracy: %.2f' % (accuracy*100))
        print('---------------------------------------')
        loss_test, accuracy_test = self.model.evaluate(self.X_test, self.y_test)
        print('Test Loss:, %.2f' % (loss_test*100))
        print('Test Accuracy: %.2f' % (accuracy_test*100))
