# Źródło problemu: https://www.codingame.com/ide/puzzle/scrabble
# Autor: Damian Rutkowski s16583

import sys
import math

letter_point_dict = {
    "e": 1,
    "a": 1,
    "i": 1,
    "o": 1,
    "n": 1,
    "r": 1,
    "t": 1,
    "l": 1,
    "s": 1,
    "u": 1,
    "d": 2,
    "g": 2,
    "b": 3,
    "c": 3,
    "m": 3,
    "p": 3,
    "f": 4,
    "h": 4,
    "v": 4,
    "w": 4,
    "y": 4,
    "k": 5,
    "j": 8,
    "x": 8,
    "q": 10,
    "z": 10
}
n = int(input())
words = []

for i in range(n):
    w = input()
    if len(w) <= 7:
        words.append(w)

letters = input()

max_points = 0
max_points_word = ""

for i in range(len(words)):
    points = 0
    remaining_letters = words[i]
    for j in range(len(letters)):
        if letters[j] in remaining_letters:
            points += letter_point_dict[letters[j]]
            remaining_letters = remaining_letters.replace(letters[j], "", 1)
            if len(remaining_letters) == 0:
                if points > max_points:
                    max_points = points
                    max_points_word = words[i]
                break

print(max_points_word)
