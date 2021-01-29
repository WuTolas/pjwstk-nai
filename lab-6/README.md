# Neural networks
  
**Authors**: Damian Rutkowski (s16583), Piotr Krajewski (s17410)

## Example run

% model evaluation:
https://www.youtube.com/watch?v=roEEZbAwM2Y

camera smile detection:

## Environment setup - linux

1. Make sure that you have **python3**, **python3-pip** and **python3-venv** installed
2. Download project, extract it and go to the **lab-6** folder
3. Create virtual environment: `python3 -m venv env`
4. Activate virtual environment: `source env/bin/activate`
5. Install the requirements: `python3 -m pip install -r requirements.txt`

## How to run the app

While being in lab-6 folder, type: `python3 main.py` and provide necessary console inputs.

## About used data

- Pima Indians Diabetes Dataset
    - https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv
    - https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.names
    Output labels included in the dataset
- CIFAR-10 dataset
    - https://www.cs.toronto.edu/%7Ekriz/cifar.html
    Output labels included in the dataset
- Fashion-MNIST
    - https://github.com/zalandoresearch/fashion-mnist
    Output labels included in the dataset
- LFWcrop Face Dataset
    - https://conradsanderson.id.au/lfwcrop/
    Output classes weren't included for the smile detection problem - at first we used information from here:
    https://data.mendeley.com/datasets/yz4v8tb3tp/5 but the first outcome wasn't satisfying for us. In fact it was detecting smiles - but one had to open the whole mouth and show the teeth.
    We classified manually around ~4 000 samples (`our-non-smile-list.txt` and `our-smile-list.txt`) with the help of `manual_classification.py` script - it might not be perfect as it could be prone to the human error, but the result was more satisfying. Also neural network layers should be fixed as sometimes when one runs this case, model can be A BIT broken (e.g. you're not smiling, yet predict outputs > 0.9). Saved model works more or less good (`smile-deep.hdf5 / smile-deep-best.hdf5`).
