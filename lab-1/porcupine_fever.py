# Źródło problemu: https://www.codingame.com/ide/puzzle/porcupine-fever
# Autor: Damian Rutkowski s16583

import sys
import math

n = int(input())
y = int(input())
cages = [[] for _ in range(n)]

for i in range(n):
    s, h, a = [int(j) for j in input().split()]
    cages[i].append(s)
    cages[i].append(h)
    cages[i].append(a)

for i in range(y):
    total_dead = 0
    total_alive = 0
    for j in range(n):
        dead = cages[j][0]
        should_be_sick = dead * 2
        new_sick = should_be_sick if should_be_sick <= cages[j][1] else cages[j][1]
        new_healthy = cages[j][2] - (dead + new_sick)
        new_alive = new_sick + new_healthy

        total_dead += dead
        total_alive += new_alive

        cages[j][0] = new_sick
        cages[j][1] = new_healthy
        cages[j][2] = new_alive

    print(total_alive)

    if total_alive == 0:
        break
