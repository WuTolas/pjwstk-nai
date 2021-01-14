# SVM for classification
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-5/README.md

from abc import ABC, abstractmethod 
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split


class SVCbase(ABC):
    """
    Abstract Support Vector Classifier model class for defining needed methods to create trained model and predict the class label output.

    Attributes
    ----------
    svc : SVC

    Methods
    -------
    prepare_classifier_model(self):
        Prepares support vector classification model - splits the data between training and test set,
        generates model with specific kernel, trains the model and prints accuracy of the model.
    prepare_data(self):
        Method should be implemented in a way which will allow SVC to use the dataframe.
        Should load and preprocess the data here.
    predict_output(self, data):
        Method should perform classification on provided one sample of data.
    """

    def prepare_classifier_model(self):
        """
        Prepares support vector classification model - splits the data between training and test set,
        generates model with specific kernel, trains the model and prints accuracy of the model.

        Returns
        -------
        None
        """
        X, y = self.prepare_data()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        svc = svm.SVC(kernel='rbf').fit(X, y)
        svc.fit(X_train, y_train)
        y_prediction = svc.predict(X_test)
        print("Classifier prepared - accuracy of the model: ", metrics.accuracy_score(y_test, y_prediction))
        self.svc = svc

    @abstractmethod
    def prepare_data(self):
        """
        Method should be implemented in a way which will allow SVM to use the dataframe.
        Should load and preprocess the data here.
        
        Returns
        -------
        X - dataframe matrix containing data without class label
        y - class labels for each data set in X
        """
        pass

    @abstractmethod
    def predict_output(self, data):
        """
        Method should perform classification on provided one sample of data.

        Parameters
        ----------
        data - 1d array

        Returns
        -------
        Class label / labels
        """
        pass
