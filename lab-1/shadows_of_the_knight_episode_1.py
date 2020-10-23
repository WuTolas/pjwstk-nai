# Źródło problemu: https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1
# Autor: Damian Rutkowski s16583

import sys
import math

w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]
ly = 0
lx = 0
ry = h - 1
rx = w - 1

while True:

    bomb_dir = input()

    if "R" in bomb_dir:
        lx = x0 + 1
    elif "L" in bomb_dir:
        rx = x0 - 1
    if "D" in bomb_dir:
        ly = y0 + 1
    elif "U" in bomb_dir:
        ry = y0 - 1

    y0 = ly + (ry - ly) // 2
    x0 = lx + (rx - lx) // 2

    print(x0, y0)
