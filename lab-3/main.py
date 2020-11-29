# Problem: Babushka fuzzy logic - how much money I should give to my grandson/granddaughter
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-3/README.md

from fuzzy_babushka import FuzzyBabushka
import math

babushka = FuzzyBabushka()

day_of_the_month = int(input("Enter day of the month (1-31): "))
high_marks = int(input("How many high marks (5's and 6's) did your grandson/granddaughter get since last visit?: "))
meals = int(input("How many meals did he/she eat?: "))

babushka.simulate(high_marks, day_of_the_month, meals)
reward = math.floor(babushka.get_output_value())

print("I should reward him/her with ", reward, ' PLN')
