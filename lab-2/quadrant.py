# Rules: https://en.wikipedia.org/wiki/Pentago
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-2/README.md

from direction import Direction
from copy import deepcopy


class Quadrant:
    """
    Class to represent a quadrant.

    Attributes
    ----------
    positions_count : int
        length of the board array
    board : 1D array[int]
        array which holds information about empty indexes or player occupied indexes - empty index has the value of 0

    Methods
    -------
    rotate(direction):
        Rotates quadrant to the left or to the right - it means that new array is created and specified positions
        changed with each other. New array is assigned to the board attribute.
    place_player(player, position):
        Places player value on provided position in the quadrant array.
    get_line(row):
        Returns quadrant line containing empty or assigned positions for displaying purpose.
    available_positions():
        Gets all available positions in the current quadrant - available position means that array value
        under some index is equal to 0. For each index we're adding +1 as people start counting from 1.
    player_to_symbol(player):
        Converts player int value to str symbol.
    get_board():
        Returns quadrant board array.
    """

    def __init__(self, positions):
        """
        Creates all attributes needed for the quadrant object.

        Parameters
        ----------
        positions : int
            number of positions in the quadrant board
        """
        self.positions_count = positions
        self.board = [0 for _ in range(self.positions_count)]

    def rotate(self, direction):
        """
        Rotates quadrant to the left or to the right - it means that new array is created and specified positions
        changed with each other. New array is assigned to the board attribute.

        Parameters
        ----------
        direction : Enum Direction
            either Direction.CLOCKWISE or Direction.ANTICLOCKWISE

        Returns
        -------
        None
        """
        new_board = deepcopy(self.board)
        if direction == Direction.CLOCKWISE:
            new_board[2] = self.board[0]
            new_board[5] = self.board[1]
            new_board[8] = self.board[2]
            new_board[1] = self.board[3]
            new_board[7] = self.board[5]
            new_board[0] = self.board[6]
            new_board[3] = self.board[7]
            new_board[6] = self.board[8]
        else:
            new_board[6] = self.board[0]
            new_board[3] = self.board[1]
            new_board[0] = self.board[2]
            new_board[7] = self.board[3]
            new_board[1] = self.board[5]
            new_board[8] = self.board[6]
            new_board[5] = self.board[7]
            new_board[2] = self.board[8]
        self.board = new_board

    def place_player(self, player, position):
        """
        Places player value on provided position in the quadrant array.

        Parameters
        ----------
        player : int
        position : int
            index of the quadrant array

        Returns
        -------
        None
        """
        self.board[position] = player

    def get_line(self, row):
        """
        Returns quadrant line containing empty or assigned positions for displaying purpose.

        Parameters
        ----------
        row : int
            which row one wants to print

        Returns
        -------
        line : str
            contains 3 index values from the board array, converted to specified symbol
        """
        line = ""
        start = row * 3
        end = start + 3
        for i in range(start, end):
            line = line + self.player_to_symbol(self.board[i])
            if i != end - 1:
                line = line + " "
        return line

    def available_positions(self):
        """
        Gets all available positions in the current quadrant - available position means that array value
        under some index is equal to 0. For each index we're adding +1 as people start counting from 1.

        Returns
        -------
        available_positions : 1D array[int]
        """
        available_positions = []
        for i in range(self.positions_count):
            if self.board[i] == 0:
                available_positions.append(i+1)
        return available_positions

    @staticmethod
    def player_to_symbol(player):
        """
        Converts player int value to str symbol.

        Parameters
        ----------
        player : int
            possible values 1 and 2

        Returns
        -------
        symbol : str
            will return _ when player int is different than 1 or 2
        """
        symbol = '_'
        if player == 1:
            symbol = 'x'
        elif player == 2:
            symbol = 'o'
        return symbol

    def get_board(self):
        """
        Returns quadrant board array.

        Returns
        -------
        board : 1D array[int]
        """
        return self.board
