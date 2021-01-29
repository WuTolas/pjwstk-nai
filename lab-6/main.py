# Neural networks
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-6/README.md

from pima_indians_neural_network import PimaIndiansNeuralNetwork
from fashion_neural_network import FashionNeuralNetwork
from cifar10_neural_network import Cifar10NeuralNetwork
from smile_neural_network import SmileNeuralNetwork


def main():
    print('Indians? : 1')
    print('Fashion? : 2')
    print('Cifar10 (Animals)?: 3')
    print('Smile?: 4')
    choice = int(input("Choose problem: "))

    if choice == 1:
        network_choice = network_choice_prompt()
        pima_ne = PimaIndiansNeuralNetwork()
        pima_ne.train_model(network_choice)
    elif choice == 2:
        network_choice = network_choice_prompt()
        fashion_ne = FashionNeuralNetwork()
        fashion_ne.train_model(network_choice)
    elif choice == 3:
        network_choice = network_choice_prompt()
        cifar_ne = Cifar10NeuralNetwork()
        load_train = load_train_prompt()
        if load_train == 1:
            cifar_ne.train_model(network_choice)
        elif load_train == 2:
            cifar_ne.load_model(network_choice)
    elif choice == 4:
        network_choice = network_choice_prompt()
        smile_ne = SmileNeuralNetwork()
        load_train = load_train_prompt()
        if load_train == 1:
            smile_ne.train_model(network_choice)
        elif load_train == 2:
            smile_ne.load_model(network_choice)
        camera_choice = str(input("Test camera (yes, no)?: "))
        if camera_choice == "yes":
            smile_ne.validate_with_camera()


def network_choice_prompt():
    print('Neural network: 1, Deep Neural Network: 2')
    return int(input("Network type: "))


def load_train_prompt():
    print('Train new model: 1, Load trained model: 2')
    return int(input("What u want to do: "))


if __name__ == "__main__":
    main()
