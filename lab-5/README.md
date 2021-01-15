# SVM Classifier
  
**Authors**: Damian Rutkowski (s16583), Piotr Krajewski (s17410)

## Example run

https://youtu.be/q1CO351x1e4

## Environment setup - linux

1. Make sure that you have **python3**, **python3-pip** and **python3-venv** installed
2. Download project, extract it and go to the **lab-5** folder
3. Create virtual environment: `python3 -m venv env`
4. Activate virtual environment: `source env/bin/activate`
5. Install the requirements: `python3 -m pip install -r requirements.txt`

## How to run the app

While being in lab-5 folder, type: `python3 main.py` and provide necessary console inputs.

Classifier models are created for the following data:
- Pima Indians Diabetes Dataset
    - https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv
    - https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.names
    Output classes (diabetes result): 0 (tested negative for diabets), 1 (tested positive for diabetes)
- Car Evaluation Dataset
    - http://archive.ics.uci.edu/ml/datasets/Car+Evaluation
    Output classes (car acceptability): unacc, acc, good, vgood
