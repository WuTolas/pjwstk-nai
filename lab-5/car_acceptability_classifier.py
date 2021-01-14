# SVM for classification
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-5/README.md
# Car evaluation data obtained from: http://archive.ics.uci.edu/ml/datasets/Car+Evaluation

import numpy as np
from svc_base import SVCbase
from sklearn import preprocessing


class CarAcceptabilityClassifier(SVCbase):
    """
    Support Vector Classifier model class for evaluating cars.

    Attributes
    ----------
    svc : SVC
    __feature_label_encoders : 1d array containing LabelEncoder
    __output_label_encoder : LabelEncoder for the output class labels

    Methods
    -------
    prepare_classifier_model(self):
        Creates all additional attributes needed for the cars SVC.
        Prepares classifier model.
    prepare_data(self):
        Loads and preprocesses the cars data to be useful for SVM classifier.
    predict_output(self, data):
        Performs classification on provided one sample of data.
    """

    def __init__(self):
        """
        Creates all additional attributes needed for the cars SVC.
        Prepares classifier model.
        """
        self.__feature_label_encoders = []
        self.__output_label_encoder = preprocessing.LabelEncoder()
        self.prepare_classifier_model()
        
    def prepare_data(self):
        """
        Loads and preprocesses the cars data to be useful for SVM classifier.
        
        Returns
        -------
        X - dataframe matrix containing data without class label
        y - class labels for each data sample in X
        """
        f = open("data/car.data")
        data = np.genfromtxt(fname = f, delimiter = ',', dtype=None, encoding=None)
        X = data[:, :-1]

        for i in range(np.shape(X)[1]):
            le = preprocessing.LabelEncoder()
            le.fit(X[:, i])
            X[:, i] = le.transform(X[:, i])
            self.__feature_label_encoders.append(le)
        
        self.__output_label_encoder.fit(data[:, -1])
        y = self.__output_label_encoder.transform(data[:, -1])

        return X, y

    def predict_output(self, data):
        """
        Performs classification on provided one sample of data.

        Parameters
        ----------
        data - 1d array

        Returns
        -------
        Class label : string

        Class labels
        ------------
        unacc - unacceptable
        acc - acceptable
        good - good
        vgood - very good
        """
        for i in range(len(data)):
            data[i] = self.__feature_label_encoders[i].transform([data[i]])[0]
        output = self.svc.predict([data])
        return self.__output_label_encoder.inverse_transform(output)[0]
