# Problem: Babushka fuzzy logic - how much money I should give to my grandson
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-3/README.md

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

plt.ioff()

# Universe variables
in_high_marks = ctrl.Antecedent(np.arange(0, 11, 1), 'high_marks')
in_day_of_the_month = ctrl.Antecedent(np.arange(0, 31, 1), 'day_of_the_month')
in_days_after_last_visit = ctrl.Antecedent(np.arange(0, 61, 1), 'days_after_last_visit')
in_meals = ctrl.Antecedent(np.arange(0, 3.5, .5), 'meals')
out_money = ctrl.Consequent(np.arange(0, 101, 1), 'Babushka Foundation')

# Fuzzy membership functions
in_high_marks['few'] = fuzz.trimf(in_high_marks.universe, [0, 0, 5])
in_high_marks['some'] = fuzz.trimf(in_high_marks.universe, [0, 5, 10])
in_high_marks['lot'] = fuzz.trimf(in_high_marks.universe, [5, 10, 10])

in_day_of_the_month['beginning'] = fuzz.trimf(in_day_of_the_month.universe, [1, 1, 15])
in_day_of_the_month['middle'] = fuzz.trimf(in_day_of_the_month.universe, [1, 15, 30])
in_day_of_the_month['end'] = fuzz.trimf(in_day_of_the_month.universe, [15, 30, 30])

in_days_after_last_visit['few'] = fuzz.trimf(in_days_after_last_visit.universe, [0, 0, 30])
in_days_after_last_visit['some'] = fuzz.trimf(in_days_after_last_visit.universe, [0, 30, 60])
in_days_after_last_visit['lot'] = fuzz.trimf(in_days_after_last_visit.universe, [30, 60, 60])

in_meals['hungry'] = fuzz.trimf(in_meals.universe, [0, 0, 1.5])
in_meals['meeeh'] = fuzz.trimf(in_meals.universe, [0, 1.5, 3])
in_meals['full'] = fuzz.trimf(in_meals.universe, [1.5, 3, 3])

out_money['homeless'] = fuzz.trimf(out_money.universe, [0, 0, 20])
out_money['motel'] = fuzz.trimf(out_money.universe, [0, 20, 40])
out_money['kowalsky'] = fuzz.trimf(out_money.universe, [20, 40, 60])
out_money['hotel'] = fuzz.trimf(out_money.universe, [40, 60, 80])
out_money['rockefeller'] = fuzz.trimf(out_money.universe, [80, 100, 100])


# POPRAWIC RULE
rule1 = ctrl.Rule(in_day_of_the_month['end'], out_money['homeless'])
rule2 = ctrl.Rule(in_day_of_the_month['middle'], out_money['kowalsky'])
rule3 = ctrl.Rule(in_day_of_the_month['beginning'], out_money['rockefeller'])

rule4 = ctrl.Rule(antecedent=(
        (in_high_marks['few'] & in_days_after_last_visit['few'] & in_meals['hungry'])),
    consequent=out_money['homeless'])

rule5 = ctrl.Rule(antecedent=(
        (in_high_marks['few'] & in_days_after_last_visit['some'] & in_meals['hungry']) |
        (in_high_marks['few'] & in_days_after_last_visit['few'] & in_meals['meeeh']) |
        (in_high_marks['few'] & in_days_after_last_visit['few'] & in_meals['full']) |
        (in_high_marks['some'] & in_days_after_last_visit['few'] & in_meals['hungry']) |
        (in_high_marks['few'] & in_days_after_last_visit['some'] & in_meals['meeeh']) |
        (in_high_marks['few'] & in_days_after_last_visit['some'] & in_meals['full']) |
        (in_high_marks['few'] & in_days_after_last_visit['lot'] & in_meals['meeeh']) |
        (in_high_marks['few'] & in_days_after_last_visit['lot'] & in_meals['hungry'])), 
    consequent=out_money['motel'])

rule6 = ctrl.Rule(antecedent=(
        (in_high_marks['lot'] & in_days_after_last_visit['few'] & in_meals['hungry']) |
        (in_high_marks['some'] & in_days_after_last_visit['some'] & in_meals['meeeh']) |
        (in_high_marks['some'] & in_days_after_last_visit['few'] & in_meals['meeeh']) |
        (in_high_marks['some'] & in_days_after_last_visit['some'] & in_meals['hungry']) | 
        (in_high_marks['some'] & in_days_after_last_visit['some'] & in_meals['full']) |
        (in_high_marks['some'] & in_days_after_last_visit['lot'] & in_meals['meeeh']) |
        (in_high_marks['some'] & in_days_after_last_visit['few'] & in_meals['full']) |
        (in_high_marks['some'] & in_days_after_last_visit['lot'] & in_meals['hungry']) |
        (in_high_marks['few'] & in_days_after_last_visit['lot'] & in_meals['full'])),
    consequent=out_money['kowalsky'])

rule7 = ctrl.Rule(antecedent=(
        (in_high_marks['lot'] & in_days_after_last_visit['lot'] & in_meals['hungry']) |
        (in_high_marks['some'] & in_days_after_last_visit['lot'] & in_meals['full']) |
        (in_high_marks['lot'] & in_days_after_last_visit['lot'] & in_meals['meeeh']) |
        (in_high_marks['lot'] & in_days_after_last_visit['some'] & in_meals['full']) |
        (in_high_marks['lot'] & in_days_after_last_visit['some'] & in_meals['meeeh']) |
        (in_high_marks['lot'] & in_days_after_last_visit['some'] & in_meals['hungry']) |
        (in_high_marks['lot'] & in_days_after_last_visit['few'] & in_meals['full']) | 
        (in_high_marks['lot'] & in_days_after_last_visit['few'] & in_meals['meeeh'])),
    consequent=out_money['hotel'])

rule8 = ctrl.Rule(antecedent=(
        (in_high_marks['lot'] & in_days_after_last_visit['lot'] & in_meals['full'])),
    consequent=out_money['rockefeller'])


babushka_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
babushka = ctrl.ControlSystemSimulation(babushka_ctrl)

babushka.input['day_of_the_month'] = 1
babushka.input['days_after_last_visit'] = 1
babushka.input['meals'] = 3
babushka.input['high_marks'] = 10

babushka.compute()

print(babushka.output['Babushka Foundation'])
# out_money.view(sim=babushka)
# plt.show()