from quadrant import Quadrant
from direction import Direction


class Board:

    def __init__(self):
        self.quadrants = 4
        self.play_area = [Quadrant() for _ in range(self.quadrants)]

    def print_board(self):
        for i in range(0, len(self.play_area), 2):
            for j in range(len(self.play_area[i].board)):
                line = self.play_area[i].get_line(j) + " | " + self.play_area[i+1].get_line(j)
                print(line)
            if i < len(self.play_area) - 2:
                print("---------------")
        print()

    def place_choice(self, choice, quadrant, y, x):
        if not self.is_valid_quadrant(quadrant):
            return False
        return self.play_area[quadrant].place_choice(choice, y, x)
    
    def rotate_quadrant(self, quadrant, direction):
        if direction == 0:
            direction = Direction.ANTICLOCKWISE
        else:
            direction = Direction.CLOCKWISE
        self.play_area[quadrant].rotate(direction)

    def is_valid_quadrant(self, quadrant):
        return 0 <= quadrant < self.quadrants

    def player_choices(self, symbol):
        current_choices = []
        for quadrant in range(self.quadrants):
            for row in range(self.play_area[quadrant].get_rows()):
                for column in range(self.play_area[quadrant].get_columns()):
                    if self.play_area[quadrant].get_board()[row][column] == symbol:
                        current_choices.append((quadrant, row, column))
        return current_choices

    def count_occupied_middles_by_symbol(self, symbol):
        count = 0
        for i in range(self.quadrants):
            if self.play_area[i].middle_occupied_by(symbol):
                count = count + 1
        return count

    def available_moves(self):
        available_moves = []
        for i in range(len(self.play_area)):
            available_coordinates = self.play_area[i].available_coordinates()
            for j in range(len(available_coordinates)):
                for k in range(len(self.play_area)):
                    y, x = available_coordinates[j]
                    available_moves.append([i, y, x, k, 0])
                    available_moves.append([i, y, x, k, 1])
        return available_moves