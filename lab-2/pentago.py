# Rules: https://en.wikipedia.org/wiki/Pentago
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-2/README.md

from board import Board
from easyAI import TwoPlayersGame, Negamax, Human_Player, AI_Player, TT


class Pentago(TwoPlayersGame):
    """
    Class to represent Pentago game.

    Extends TwoPlayersGame class from the easyAI library.

    https://en.wikipedia.org/wiki/Pentago

    Attributes
    ----------
    board : Board
        board containing quadrants from which it is made
    players : 1D array[Human_Player/AI_Player]
        players participating in the game - 2 values
    nplayer : int
        current player making move
    has_lost : bool
        contains information whether the current player has lost
    end_before_rotate : bool
        contains information whether the game ended before rotating the quadrant

    Methods
    -------
    make_move(move):
        Performs move on the game board.
    unmake_move(move):
        Undoes move performed by AI - speeds up the AI.
    ttentry():
        Generates transposition table - returns game state in the simple form.
    __check_win():
        Checks if the current player has winning combination.
    __check_lose():
        Checks if the opponent has winning combination.
    __winning_combination_exists(choices):
        Check whether winning combination exists in the current choices.
    possible_moves():
        Returns all possible moves which player/AI can make in the next move.
    show():
        Should print current game state before next move.
    is_over():
        Checks if the game is over.
    scoring():
        Calculates score for the current AI move outcome.
    __win_combinations():
        Returns all win combinations.
    __show_hint_table():
        Prints game positions hints table.
    """
    def __init__(self, players):
        """
        Creates all attributes needed for the pentago game object.

        Parameters
        ----------
        players : 1D array[Human_Player/AI_Player]
        """
        self.board = Board()
        self.players = players
        self.nplayer = 1
        self.has_lost = None
        self.end_before_rotate = False

    def make_move(self, move):
        """
        Performs move on the game board.
        More information at: https://zulko.github.io/easyAI/ref.html

        Parameters
        ----------
        move : str
            e.g. "20 2 l"

        Returns
        -------
        None
        """
        position, quadrant, rotate = move.split(" ")
        self.board.place_player(self.nplayer, int(position) - 1)
        if self.__check_win():
            self.end_before_rotate = True
        else:
            self.board.rotate_quadrant(int(quadrant) - 1, rotate)

    def unmake_move(self, move):
        """
        Undoes move performed by AI - speeds up the AI.
        More info at: https://zulko.github.io/easyAI/speedup.html

        Parameters
        ----------
        move : str
            e.g. "20 2 l"

        Returns
        -------
        None
        """
        position, quadrant, rotate = move.split(" ")
        if not self.end_before_rotate:
            if rotate == "l":
                rotate = "r"
            else:
                rotate = "l"
            self.board.rotate_quadrant(int(quadrant) - 1, rotate)
        else:
            self.end_before_rotate = False
        self.board.place_player(0, int(position) - 1)

    def ttentry(self):
        """
        Generates transposition table - returns game state in the simple form.

        "Transposition tables store the values of already-computed moves and positions so that if the AI meets
        them again it will win time."
        More info at: https://zulko.github.io/easyAI/speedup.html

        Returns
        -------
        tuple : tuple(int)
        """
        return tuple(value for obj in self.board.get_play_area() for value in obj.get_board())

    def __check_win(self):
        """
        Checks if the current player has winning combination.

        :return:
        """
        return self.__winning_combination_exists(self.board.player_choices(self.nplayer))

    def __check_lose(self):
        """
        Checks if the opponent has winning combination.

        Returns
        -------
        has_lost : bool
        """
        self.has_lost = self.__winning_combination_exists(self.board.player_choices(self.nopponent))
        return self.has_lost

    def __winning_combination_exists(self, choices):
        """
        Check whether winning combination exists in the current choices.

        Parameters
        ----------
        choices : 1D array[int]

        Returns
        -------
        combination_exists : bool
        """
        combination_exists = False
        for winning_combination in self.__win_combinations():
            if set(winning_combination).issubset(set(choices)):
                combination_exists = True
                break
        return combination_exists

    def possible_moves(self):
        """
        Returns all possible moves which player/AI can make in the next move.
        More info at : https://zulko.github.io/easyAI/ref.html

        Returns
        -------
        array : 1D array[int]
        """
        return self.board.available_moves()

    def show(self):
        """
        Should print current game state before next move.
        More info at: https://zulko.github.io/easyAI/ref.html

        Returns
        -------
        None
        """
        self.__show_hint_table()
        self.board.print_board()

    def is_over(self):
        """
        Checks if the game is over.
        More info at: https://zulko.github.io/easyAI/ref.html

        Returns
        -------
        is_over : bool
            True if game over False when not over
        """
        return self.__check_lose() or (self.possible_moves() == [])

    def scoring(self):
        """
        Calculates score for the current AI move outcome. Uses has_lost attribute to avoid redundant check_lose()
        calculation. Speeds up AI a bit.
        More info at: https://zulko.github.io/easyAI/speedup.html

        Returns
        -------
        scoring : int
        """
        if self.has_lost is not None:
            has_lost = self.has_lost
            self.has_lost = None
            return -100 if has_lost else 0
        else:
            return -100 if self.__check_lose() else 0

    @staticmethod
    def __win_combinations():
        """
        Returns all win combinations.

        Returns
        -------
        array : 2D array[int]
        """
        return [[1, 2, 3, 10, 11],
                [2, 3, 10, 11, 12],
                [4, 5, 6, 13, 14],
                [5, 6, 13, 14, 15],
                [7, 8, 9, 16, 17, 18],
                [8, 9, 16, 17, 18],
                [19, 20, 21, 28, 29],
                [20, 21, 28, 29, 30],
                [22, 23, 24, 31, 32],
                [23, 24, 31, 32, 33],
                [25, 26, 27, 34, 35],
                [26, 27, 34, 35, 36],
                [1, 4, 7, 19, 22, 25],
                [4, 7, 19, 22, 25],
                [2, 5, 8, 20, 23, 26],
                [5, 8, 20, 23, 26],
                [3, 6, 9, 21, 24],
                [6, 9, 21, 24, 27],
                [10, 13, 16, 28, 31],
                [13, 16, 28, 31, 34],
                [11, 14, 17, 29, 32],
                [14, 17, 29, 32, 35],
                [12, 15, 18, 30, 33],
                [15, 18, 30, 33, 36],
                [4, 8, 21, 31, 35],
                [1, 5, 9, 28, 32],
                [5, 9, 28, 32, 36],
                [2, 6, 16, 29, 33],
                [22, 20, 9, 13, 11],
                [25, 23, 21, 16, 14],
                [23, 21, 16, 14, 12],
                [26, 24, 28, 17, 15]]

    @staticmethod
    def __show_hint_table():
        """
        Prints game positions hints table.

        Returns
        -------
        None
        """
        print("Positions hint:")
        print()
        print(" 1  2  3 | 10 11 12")
        print(" 4  5  6 | 13 14 15")
        print(" 7  8  9 | 16 17 18")
        print("--------------------")
        print("19 20 21 | 28 29 30")
        print("22 23 24 | 31 32 33")
        print("25 26 27 | 34 35 36")
        print()
        print("Example move: 14 1 r")
        print("Places player on 14th position, and rotates 1st quadrant to the right")
        print()


algo = Negamax(3, tt=TT())
game = Pentago([Human_Player(), AI_Player(algo)])
game.play()
print("Player %d loses" % game.nplayer)
