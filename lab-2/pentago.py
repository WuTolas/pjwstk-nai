from board import Board
from easyAI import TwoPlayersGame, Negamax, Human_Player, AI_Player


class Pentago(TwoPlayersGame):

    def __init__(self, players):
        self.board = Board()
        self.players = players
        self.nplayer = 1
        self.end_before_rotate = False
        self.has_lost = False

    def make_move(self, move):
        position, quadrant, rotate = move
        self.board.place_player(self.nplayer, position - 1)
        if self.check_win():
            self.end_before_rotate = True
            return
        self.board.rotate_quadrant(quadrant - 1, rotate - 1)

    def unmake_move(self, move):
        position, quadrant, rotate = move
        if not self.end_before_rotate:
            if rotate == 2:
                rotate = 1
            else:
                rotate = 2
            self.board.rotate_quadrant(quadrant - 1, rotate - 1)
        else:
            self.end_before_rotate = False
        self.board.place_player(0, position - 1)

    def check_win(self):
        return self.winning_combination_exists(self.board.player_choices(self.nplayer))

    def check_lose(self):
        self.has_lost = self.winning_combination_exists(self.board.player_choices(self.nopponent))
        return self.has_lost

    def winning_combination_exists(self, choices):
        combination_exists = False
        for winning_combination in self.win_combinations():
            if set(winning_combination).issubset(set(choices)):
                combination_exists = True
                break
        return combination_exists

    def possible_moves(self):
        return self.board.available_moves()

    def show(self):
        self.board.print_board()

    def is_over(self):
        return (self.possible_moves() == []) or self.check_lose()

    def scoring(self):
        if self.has_lost:
            has_lost = self.has_lost
            self.has_lost = False
            return -100 if has_lost else 0
        else:
            return -100 if self.check_lose() else 0

    @staticmethod
    def win_combinations():
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


algo = Negamax(2)
game = Pentago([Human_Player(), AI_Player(algo)])
game.play()
