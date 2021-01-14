# SVM for classification
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-5/README.md

import numpy as np
from sklearn import svm, metrics, preprocessing
from sklearn.model_selection import train_test_split
from car_acceptability_classifier import CarAcceptabilityClassifier
from pima_indians_diabetes_classifier import PimaIndiansDiabetesClassifier


def main():
    """
    App main method.
    """
    print('Which example would you like to run?')
    choice = int(input("type 1 to go to indians, type 2 to go to car evaluation: "))
    classifier = None
    data = None

    if choice == 1:
        classifier = PimaIndiansDiabetesClassifier()
        data = get_indian_details()
    elif choice == 2:
        classifier = CarAcceptabilityClassifier()
        data = get_car_details()
    else:
        raise ValueError("choice not accessible")
    
    print("Output class: ", classifier.predict_output(data))


def get_indian_details():
    """
    Gets input from the user and returns 1d array containing details about pima indians

    Returns
    -------
    1d array
    """
    print('Provide additional detail as follows (only numeric): ')
    pregnant = int(input('Number of times pregnant: '))
    glucose_concentration = int(input('Plasma glucose concentration a 2 hours in an oral glucose tolerance test: '))
    pressure = int(input('Diastolic blood pressure (mm Hg): '))
    skin_thickness = int(input('Triceps skin fold thickness (mm): '))
    insulin = int(input('2-Hour serum insulin (mu U/ml): '))
    body_mass = float(input('Body mass index (weight in kg/(height in m)^2): '))
    diabetes = float(input('Diabetes pedigree function: '))
    age = int(input('Age in years: '))
    return np.array([pregnant, glucose_concentration, pressure, skin_thickness, insulin, body_mass, diabetes, age])


def get_car_details():
    """
    Gets input from the user and returns 1d array containing details about car
    
    Returns
    -------
    1d array
    """
    print('Provide additional detail as follows:')
    buying_price = str(input('Buying price (vhigh, high, med, low): '))
    maintenance_price = str(input('Price of the maintenance (vhigh, high, med, low): '))
    no_of_doors = str(input('Number of doors (2, 3, 4, 5more): '))
    capacity = str(input('Persons capacity in terms of persons to carry (2, 4, more): '))
    luggage = str(input('Size of luggage boot (small, med, big): '))
    safety = str(input('Estimated safety of the car (low, med, high): '))
    return np.array([buying_price, maintenance_price, no_of_doors, capacity, luggage, safety])


if __name__ == "__main__":
    main()