# Rules: https://en.wikipedia.org/wiki/Pentago
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-2/README.md

from enum import Enum


class Direction(Enum):
    """
    Enum class containing possible direction values.
    """
    CLOCKWISE = "r"
    ANTICLOCKWISE = "l"
