# Problem: Babushka fuzzy logic - how much money I should give to my grandson/granddaughter
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-3/README.md

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class FuzzyBabushka:
    """
    Class to represent a grandmom fuzzy logic - how much money grandmom should give to her grandson/granddaughter?

    Attributes
    ----------
    high_marks : Antecedent
        holds data related to the amount of received high marks
    day_of_the_month : Antacedent
        holds data related to the day of the month
    meals : Antacedent
        holds data related to the amount of eaten meals
    money : Consequent
        hold data related to the amount of money to be given

    Methods
    -------
    __prepare_universe_objects():
        Prepares objects to hold the universe variables and membership functions.
    __prepare_membership_functions():
        Prepares fuzzy membership functions.
    __prepare_rules():
        Prepares rules on which fuzzy logic calculations will be made - fuzzy relationships between inputs and output.
    __create_control_system_simulator():
        Creates control system on which specific set of rules will be applied.
    simulate(high_marks, day_of_the_month, meals):
        Calculates how much money Babushka should give to grandson/granddaughter based on the provided parameters.
    get_output_value():
        Returns how much money Babushka should give to grandson/granddaughter.
    """
    def __init__(self):
        """
        Creates all attributes needed for the fuzzy babushka object.
        """
        self.__prepare_universe_objects()
        self.__prepare_membership_functions()
        self.__prepare_rules()
        self.__create_control_system_simulator()

    def __prepare_universe_objects(self):
        """
        Prepares objects to hold the universe variables and membership functions.

        Returns
        -------
        None
        """
        self.high_marks = ctrl.Antecedent(np.arange(0, 11, 1), 'High marks')
        self.day_of_the_month = ctrl.Antecedent(np.arange(1, 32, 1), 'Day of the month')
        self.meals = ctrl.Antecedent(np.arange(0, 3, 1), 'Meals')
        self.money = ctrl.Consequent(np.arange(0, 101, 1), 'Babushka Foundation')

    def __prepare_membership_functions(self):
        """
        Prepares fuzzy membership functions.

        Returns
        -------
        None
        """
        self.high_marks['few'] = fuzz.trimf(self.high_marks.universe, [0, 0, 5])
        self.high_marks['some'] = fuzz.trimf(self.high_marks.universe, [0, 5, 10])
        self.high_marks['lot'] = fuzz.trimf(self.high_marks.universe, [5, 10, 10])

        self.day_of_the_month['beginning'] = fuzz.trimf(self.day_of_the_month.universe, [1, 1, 16])
        self.day_of_the_month['middle'] = fuzz.trimf(self.day_of_the_month.universe, [1, 16, 31])
        self.day_of_the_month['end'] = fuzz.trimf(self.day_of_the_month.universe, [16, 31, 31])

        self.meals['hungry'] = fuzz.trimf(self.meals.universe, [0, 0, 1])
        self.meals['semi-full'] = fuzz.trimf(self.meals.universe, [0, 1, 2])
        self.meals['full'] = fuzz.trimf(self.meals.universe, [1, 2, 2])

        self.money['homeless'] = fuzz.trimf(self.money.universe, [0, 0, 20])
        self.money['motel'] = fuzz.trimf(self.money.universe, [0, 20, 40])
        self.money['kowalsky'] = fuzz.trimf(self.money.universe, [20, 40, 60])
        self.money['hotel'] = fuzz.trimf(self.money.universe, [40, 60, 80])
        self.money['rockefeller'] = fuzz.trimf(self.money.universe, [80, 100, 100])

    def __prepare_rules(self):
        """
        Prepares rules on which fuzzy logic calculations will be made - fuzzy relationships between inputs and output.

        Returns
        -------
        None
        """
        self.rules = []

        rule1 = ctrl.Rule(antecedent=(
                (self.high_marks['few'] & self.day_of_the_month['end'] & self.meals['hungry'])),
            consequent=self.money['homeless'])
        self.rules.append(rule1)

        rule2 = ctrl.Rule(antecedent=(
                (self.high_marks['few'] & self.day_of_the_month['middle'] & self.meals['hungry']) |
                (self.high_marks['few'] & self.day_of_the_month['end'] & self.meals['semi-full']) |
                (self.high_marks['few'] & self.day_of_the_month['end'] & self.meals['full']) |
                (self.high_marks['some'] & self.day_of_the_month['end'] & self.meals['hungry']) |
                (self.high_marks['few'] & self.day_of_the_month['middle'] & self.meals['semi-full']) |
                (self.high_marks['few'] & self.day_of_the_month['middle'] & self.meals['full']) |
                (self.high_marks['few'] & self.day_of_the_month['beginning'] & self.meals['semi-full']) |
                (self.high_marks['few'] & self.day_of_the_month['beginning'] & self.meals['hungry'])), 
            consequent=self.money['motel'])
        self.rules.append(rule2)

        rule3 = ctrl.Rule(antecedent=(
                (self.high_marks['lot'] & self.day_of_the_month['end'] & self.meals['hungry']) |
                (self.high_marks['some'] & self.day_of_the_month['middle'] & self.meals['semi-full']) |
                (self.high_marks['some'] & self.day_of_the_month['end'] & self.meals['semi-full']) |
                (self.high_marks['some'] & self.day_of_the_month['middle'] & self.meals['hungry']) | 
                (self.high_marks['some'] & self.day_of_the_month['middle'] & self.meals['full']) |
                (self.high_marks['some'] & self.day_of_the_month['beginning'] & self.meals['semi-full']) |
                (self.high_marks['some'] & self.day_of_the_month['end'] & self.meals['full']) |
                (self.high_marks['some'] & self.day_of_the_month['beginning'] & self.meals['hungry']) |
                (self.high_marks['few'] & self.day_of_the_month['beginning'] & self.meals['full'])),
            consequent=self.money['kowalsky'])
        self.rules.append(rule3)

        rule4 = ctrl.Rule(antecedent=(
                (self.high_marks['lot'] & self.day_of_the_month['beginning'] & self.meals['hungry']) |
                (self.high_marks['some'] & self.day_of_the_month['beginning'] & self.meals['full']) |
                (self.high_marks['lot'] & self.day_of_the_month['beginning'] & self.meals['semi-full']) |
                (self.high_marks['lot'] & self.day_of_the_month['middle'] & self.meals['full']) |
                (self.high_marks['lot'] & self.day_of_the_month['middle'] & self.meals['semi-full']) |
                (self.high_marks['lot'] & self.day_of_the_month['middle'] & self.meals['hungry']) |
                (self.high_marks['lot'] & self.day_of_the_month['end'] & self.meals['full']) | 
                (self.high_marks['lot'] & self.day_of_the_month['end'] & self.meals['semi-full'])),
            consequent=self.money['hotel'])
        self.rules.append(rule4)

        rule5 = ctrl.Rule(antecedent=(
                (self.high_marks['lot'] & self.day_of_the_month['beginning'] & self.meals['full'])),
            consequent=self.money['rockefeller'])
        self.rules.append(rule5)

    def __create_control_system_simulator(self):
        """
        Creates control system on which specific set of rules will be applied.

        Returns
        -------
        None
        """
        system = ctrl.ControlSystem(self.rules)
        self.__simulator = ctrl.ControlSystemSimulation(system)

    def simulate(self, high_marks, day_of_the_month, meals):
        """
        Calculates how much money Babushka should give to grandson/granddaughter based on the provided parameters.

        Parameters
        ----------
        high_marks : int
            number of the high marks received since last visit
        day_of_the_month : int
            number of the day e.g. 16
        meals : int
            number of meals eaten

        Returns
        -------
        None 
        """
        self.__simulator.input['Day of the month'] = day_of_the_month
        self.__simulator.input['High marks'] = high_marks
        self.__simulator.input['Meals'] = meals
        self.__simulator.compute()

    def get_output_value(self):
        """
        Returns how much money Babushka should give to grandson/granddaughter.

        Returns
        -------
        money : double
        """
        return self.__simulator.output['Babushka Foundation']
