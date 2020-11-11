from quadrant import Quadrant
from direction import Direction

class Board():

    def __init__(self):
        self.playarea = [Quadrant(), Quadrant(), Quadrant(), Quadrant()]

    def print_board(self):
        quadrant_pairs_count = len(self.playarea) - 1
        for i in range(0, quadrant_pairs_count, 2):
            for j in range(len(self.playarea[i].board)):
                line = ""
                line = self.playarea[i].get_line(j) + " | " + self.playarea[i+1].get_line(j)
                print(line)
            if i != quadrant_pairs_count - 1:
                print("---------------")
            else:
                print()


    def place_choice(self, choice, quadrant, y, x):
        return self.playarea[quadrant].place_choice(choice, y, x)
    
    def rotate_quadrant(self, quadrant, direction):
        if direction == 0:
            direction = Direction.ANTICLOCKWISE
        else:
            direction = Direction.CLOCKWISE
        self.playarea[quadrant].rotate(direction)

    