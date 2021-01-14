# SVM for classification
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-5/README.md
# Data download: https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv
# More info: https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.names 

import numpy as np
from svc_base import SVCbase


class PimaIndiansDiabetesClassifier(SVCbase):
    """
    Support Vector Classifier model class for defining whether Pima Indian has diabets or not.

    Attributes
    ----------
    svc : SVC

    Methods
    -------
    prepare_classifier_model(self):
        Prepares classifier model.
    prepare_data(self):
        Loads and preprocesses the cars data to be useful for SVM classifier.
    predict_output(self, data):
        Performs classification on provided one sample of data.
    """

    def __init__(self):
        """
        Prepares classifier model.
        """
        self.prepare_classifier_model()
        
    def prepare_data(self):
        """
        Loads and preprocesses the cars data to be useful for SVM classifier.
        
        Returns
        -------
        X - dataframe matrix containing data without class label
        y - class labels for each data sample in X
        """
        f = open("data/prima-indians-diabetes.csv")
        data = np.genfromtxt(fname = f, delimiter = ',')
        X = data[:, :-1]
        y = data[:, -1]

        return X, y

    def predict_output(self, data):
        """
        Performs classification on provided one sample of data.

        Parameters
        ----------
        data - 1d array

        Returns
        -------
        Class label : int

        Class labels
        ------------
        0 - tested negative for diabetes
        1 - tested positive for diabetes
        """
        return int(self.svc.predict([data])[0])
