from choice import Choice
from direction import Direction
from copy import deepcopy


class Quadrant:

    def __init__(self):
        self.columns = 3
        self.rows = 3
        self.board = [[Choice.EMPTY for _ in range(self.columns)] for _ in range(self.rows)]
    
    def rotate(self, direction):
        new_board = deepcopy(self.board)
        if direction == Direction.CLOCKWISE:
            new_board[0][0] = self.board[2][0]
            new_board[0][1] = self.board[1][0]
            new_board[0][2] = self.board[0][0]
            new_board[1][0] = self.board[2][1]
            new_board[1][2] = self.board[0][1]
            new_board[2][0] = self.board[2][2]    
            new_board[2][1] = self.board[1][2]
            new_board[2][2] = self.board[0][2]
        else:
            new_board[0][0] = self.board[0][2]
            new_board[0][1] = self.board[1][2]
            new_board[0][2] = self.board[2][2]
            new_board[1][2] = self.board[2][1]
            new_board[2][2] = self.board[2][0]
            new_board[2][1] = self.board[1][0]
            new_board[2][0] = self.board[0][0]
            new_board[1][0] = self.board[0][1]              
        self.board = new_board

    def is_empty(self, y, x):
        return self.board[y][x] == Choice.EMPTY

    def place_choice(self, choice, y, x):
        result = False
        if self.is_valid_coordinate(y, x) and self.is_empty(y, x):
            self.board[y][x] = choice
            result = True
        return result

    def get_line(self, row):
        line = ""
        for i in range(len(self.board[row])):
            line = line + self.board[row][i].value
            if i != len(self.board[row]):
                line = line + " "
        return line

    def is_valid_coordinate(self, y, x):
        valid = True
        if y < 0 or x < 0:
            valid = False
        if y > self.rows or x > self.columns:
            valid = False
        return valid

    def available_coordinates(self):
        available_coordinates = []
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.is_empty(row, column):
                    available_coordinates.append([row, column])
        return available_coordinates

    def get_board(self):
        return self.board

    def get_columns(self):
        return self.columns

    def get_rows(self):
        return self.rows