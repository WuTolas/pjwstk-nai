# Neural networks
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-6/README.md
# Data download: https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv
# More info: https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.names 

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
import tensorflow as tf
from tensorflow import keras


class PimaIndiansNeuralNetwork():
    """
    Neural network class for detecting diabetes.

    # Classifier from the previous task
    # Accuracy of the model:  0.7402597402597403

    # 'Normal'
    # Train Loss:, 50.31
    # Train Accuracy: 78.03
    # ---------------------------------------
    # Test Loss:, 54.77
    # Test Accuracy: 71.86

    # Train Loss:, 40.13
    # Train Accuracy: 80.26
    ---------------------------------------
    # Test Loss:, 60.48
    # Test Accuracy: 71.86

    Attributes
    ----------
    model : Model
    X_train : ndarray containing train data
    y_train : array containing train output labels
    X_test : ndarray containing test data
    y_test : array containing test output labels

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
        f = open("data/pima/pima-indians-diabetes.csv")
        data = np.genfromtxt(fname = f, delimiter = ',')
        X = data[:, :-1]
        y = data[:, -1]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3)
    
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
        self.model.add(keras.layers.Input(8))
        self.model.add(keras.layers.Dense(6, activation='relu'))
        self.model.add(keras.layers.Dense(1, activation='sigmoid'))

    def __prepare_deep_neural_network_model(self):
        """
        Prepares model, creates layers.

        Returns
        -------
        None
        """
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.Input(8))
        self.model.add(keras.layers.Dense(12, activation='relu'))
        self.model.add(keras.layers.Dense(8, activation='relu'))
        self.model.add(keras.layers.Dense(4, activation='relu'))
        self.model.add(keras.layers.Dense(1, activation='sigmoid'))

    def __compile_fit(self):
        """
        Compiles and trains the model.

        Returns
        -------
        None
        """
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.model.fit(self.X_train, self.y_train, epochs=1000, batch_size=32)

    def __evaluate(self):
        """
        Evaluates model - prints loss and accuracy values for train and test sets.

        Returns
        -------
        None
        """
        print('Evaluating pima indians neural network...')
        loss, accuracy = self.model.evaluate(self.X_train, self.y_train)
        print('Train Loss:, %.2f' % (loss*100))
        print('Train Accuracy: %.2f' % (accuracy*100))
        print('---------------------------------------')
        loss, accuracy = self.model.evaluate(self.X_test, self.y_test)
        print('Test Loss:, %.2f' % (loss*100))
        print('Test Accuracy: %.2f' % (accuracy*100))
