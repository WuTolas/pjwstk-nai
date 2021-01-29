# Neural networks
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-6/README.md

import os
import cv2
from pathlib import Path
import sys


def main():
    file_names = sorted(os.listdir("./data/smile/faces/"))
    start_at = file_length("./data/smile/our-cancelled-list.txt") + file_length("./data/smile/our-smile-list.txt") + file_length("./data/smile/our-non-smile-list.txt")

    for name in file_names[start_at:]:
        full_file_path = "./data/smile/faces/" + name.strip()
        if Path(full_file_path):
            image = cv2.imread(full_file_path)
            cv2.imshow("img", image)
            while True:
                k = cv2.waitKey(0)
                if k == 27:
                    sys.exit()
                if k == 115:
                    with open("./data/smile/our-cancelled-list.txt", "a") as f:
                        f.write(name + "\n")
                    break
                elif k == 116:
                    with open("./data/smile/our-smile-list.txt", "a") as f:
                        f.write(name + "\n")
                    break
                elif k == 110:
                    with open("./data/smile/our-non-smile-list.txt", "a") as f:
                        f.write(name + "\n")
                    break


def file_length(file_name):
    i = None
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    if i is None:
        return 0
    else:
        return i + 1


if __name__ == "__main__":
    main()