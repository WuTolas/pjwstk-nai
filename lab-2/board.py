# Rules: https://en.wikipedia.org/wiki/Pentago
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-2/README.md

from quadrant import Quadrant
from direction import Direction


class Board:
    """
    Class to represent board.

    Attributes
    ----------
    quadrants_count : int
        number of the quadrants in the play_area attribute
    quadrant_positions_count : int
        number of the positions per quadrant
    play_area : 1D array[Quadrant]
        array containing quadrant objects

    Methods
    -------
    print_board():
        Prints all quadrants.
    place_player(player, position):
        Places player in the specific quadrant. Quadrant and array index are calculated based on the integers division
        (quadrant value) and integers remainder (array index value).
    rotate_quadrant(quadrant, direction):
        Rotates selected quadrant in specific direction - either left or right. Calls Quadrant method.
    player_choices(player):
        Generates specific player positions on the whole play area. Values are based on which quadrant position is held.
        First quadrant might contain values from 1 to 9, next quadrant might contain values from 10 to 18 etc.
    available_moves():
        Generates all available moves, from all quadrants, which player can make. First quadrant might contain values
        from 1 to 9, next quadrant might contain values from 10 to 18 etc.
    get_play_area():
        Returns play area array containing Quadrant objects.
    """

    def __init__(self):
        """
        Creates all attributes needed for the board object.
        """
        self.quadrants_count = 4
        self.quadrant_positions_count = 9
        self.play_area = [Quadrant(self.quadrant_positions_count) for _ in range(self.quadrants_count)]

    def print_board(self):
        """
        Prints all quadrants.

        Returns
        -------
        None
        """
        for i in range(0, self.quadrants_count, 2):
            for row in range(3):
                line = self.play_area[i].get_line(row) + " | " + self.play_area[i+1].get_line(row)
                print(line)
            if i < self.quadrants_count - 2:
                print("----------------")

    def place_player(self, player, position):
        """
        Places player in the specific quadrant. Quadrant and array index are calculated based on the integers division
        (quadrant value) and integers remainder (array index value).

        Parameters
        ----------
        player : int
        position : int
            values from 1
        """
        quadrant = position // self.quadrant_positions_count
        quadrant_position = position % self.quadrant_positions_count
        self.play_area[quadrant].place_player(player, quadrant_position)
    
    def rotate_quadrant(self, quadrant, direction):
        """
        Rotates selected quadrant in specific direction - either left or right. Calls Quadrant method.

        Parameters
        ----------
        quadrant : int
            values from 0
        direction : str
            either 'l' or 'r'

        Returns
        -------
        None
        """
        direction = Direction(direction)
        self.play_area[quadrant].rotate(direction)

    def player_choices(self, player):
        """
        Generates specific player positions on the whole play area. Values are based on which quadrant position is held.
        First quadrant might contain values from 1 to 9, next quadrant might contain values from 10 to 18 etc.

        Parameters
        ----------
        player : int

        Returns
        -------
        player_choices : 1D array[int]
        """
        player_choices = []
        for i in range(self.quadrants_count):
            quadrant_board = self.play_area[i].get_board()
            for j in range(self.quadrant_positions_count):
                if quadrant_board[j] == player:
                    position = j + 1 + i * 9
                    player_choices.append(position)
        return player_choices

    def available_moves(self):
        """
        Generates all available moves, from all quadrants, which player can make. First quadrant might contain values
        from 1 to 9, next quadrant might contain values from 10 to 18 etc.

        Returns
        -------
        available_moves : 1D array[str]
            contains information about available moves - what position is empty, which quadrant can u rotate and
            direction of the rotate - e.g. '10 2 l'

        """
        available_moves = []
        for i in range(self.quadrants_count):
            quadrant_positions = self.play_area[i].available_positions()
            for p in quadrant_positions:
                position = p + i * 9
                for j in range(self.quadrants_count):
                    move1 = [str(position), str(j + 1), "l"]
                    move2 = [str(position), str(j + 1), "r"]
                    available_moves.append(" ".join(move1))
                    available_moves.append(" ".join(move2))
        return available_moves

    def get_play_area(self):
        """
        Returns play area array containing Quadrant objects.

        Returns
        -------
        play_area : 1D array[Quadrant]
        """
        return self.play_area
