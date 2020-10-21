# Źródło problemu: https://www.codingame.com/ide/puzzle/the-descent
# Autor: Damian Rutkowski s16583

import sys
import math

while True:
    highest_index = 0
    highest_mountain = 0
    for i in range(8):
        mountain_h = int(input())
        if mountain_h > highest_mountain:
            highest_mountain = mountain_h
            highest_index = i

    print(highest_index)
