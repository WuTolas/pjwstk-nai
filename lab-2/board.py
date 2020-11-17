from quadrant import Quadrant
from direction import Direction


class Board:

    def __init__(self):
        self.quadrants_count = 4
        self.play_area = [Quadrant() for _ in range(self.quadrants_count)]

    def print_board(self):
        for i in range(0, self.quadrants_count, 2):
            for row in range(3):
                line = self.play_area[i].get_line(row) + " | " + self.play_area[i+1].get_line(row)
                print(line)
            if i < self.quadrants_count - 2:
                print("----------------")

    def place_player(self, player, position):
        quadrant = position // 9
        quadrant_position = position % 9
        return self.play_area[quadrant].place_player(player, quadrant_position)
    
    def rotate_quadrant(self, quadrant, direction):
        if direction == 0:
            direction = Direction.ANTICLOCKWISE
        else:
            direction = Direction.CLOCKWISE
        self.play_area[quadrant].rotate(direction)

    def player_choices(self, player):
        player_choices = []
        for i in range(self.quadrants_count):
            quadrant_board = self.play_area[i].get_board()
            positions_count = self.play_area[i].get_positions_count()
            for j in range(positions_count):
                if quadrant_board[j] == player:
                    position = j + 1 + i * 9
                    player_choices.append(position)
        return player_choices

    def available_moves(self):
        available_moves = []
        for i in range(self.quadrants_count):
            quadrant_positions = self.play_area[i].available_positions()
            for p in quadrant_positions:
                position = p + i * 9
                for j in range(self.quadrants_count):
                    available_moves.append([position, j + 1, 1])
                    available_moves.append([position, j + 1, 2])
        return available_moves
