from direction import Direction
from copy import deepcopy


class Quadrant:

    def __init__(self, positions):
        self.positions_count = positions
        self.board = [0 for _ in range(self.positions_count)]

    def rotate(self, direction):
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

    def place_player(self, player, spot):
        self.board[spot] = player

    def get_line(self, row):
        line = ""
        start = row * 3
        end = start + 3
        for i in range(start, end):
            line = line + self.player_to_symbol(self.board[i])
            if i != end - 1:
                line = line + " "
        return line

    def available_positions(self):
        available_positions = []
        for i in range(self.positions_count):
            if self.board[i] == 0:
                available_positions.append(i+1)
        return available_positions

    @staticmethod
    def player_to_symbol(player):
        symbol = '_'
        if player == 1:
            symbol = 'x'
        elif player == 2:
            symbol = 'o'
        return symbol

    def get_board(self):
        return self.board

    def get_positions_count(self):
        return self.positions_count
