from choice import Choice
from direction import Direction
from copy import deepcopy

class Quadrant():

    def __init__(self):
        self.board = [[Choice.EMPTY for _ in range(3)] for _ in range(3)]
    
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
        if self.is_empty(y, x):
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
