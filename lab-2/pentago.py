from board import Board
from choice import Choice
from easyAI import TwoPlayersGame, Negamax, Human_Player, AI_Player


class Pentago(TwoPlayersGame):

    def __init__(self, players):
        self.board = Board()
        self.players = players
        self.nplayer = 1
        self.end_before_rotate = False

    def make_move(self, move):
        quadrant_before, y, x, quadrant_after, rotate = move
        player_symbol = self.get_player_symbol(self.nplayer)
        self.board.place_choice(player_symbol, quadrant_before, y, x)
        if self.check_win == True:
            self.end_before_rotate = True
            return
        self.board.rotate_quadrant(quadrant_after, rotate)

    def unmake_move(self, move):
        quadrant_before, y, x, quadrant_after, rotate = move
        player_symbol = Choice.EMPTY
        if rotate == 0:
            rotate = 1
        else:
            rotate = 0
        if self.end_before_rotate == False:
            self.board.rotate_quadrant(quadrant_after, rotate)
        else:
            self.end_before_rotate = False
        self.board.place_choice(player_symbol, quadrant_before, y, x)

    def check_win(self):
        did_i_win = False
        player_symbol = self.get_player_symbol(self.nplayer)
        player_choices = self.board.player_choices(player_symbol)
        for winning_combination in self.win_combinations():
            if set(winning_combination).issubset(set(player_choices)):
                did_i_win = True
                break
        return did_i_win

    def check_lose(self):
        did_i_lose = False
        player_symbol = self.get_player_symbol(self.nopponent)
        player_choices = self.board.player_choices(player_symbol)
        for winning_combination in self.win_combinations():
            if set(winning_combination).issubset(set(player_choices)):
                did_i_lose = True
                break
        return did_i_lose

    def possible_moves(self):
        return self.board.available_moves()

    def show(self):
        self.board.print_board()

    def is_over(self):
        return (self.possible_moves() == []) or self.end_before_rotate == True or self.check_lose()

    def scoring(self):
        score = 0
        score = score + self.board.count_occupied_middles_by_symbol(Choice.CIRCLE) * (30)
        score = score + self.board.count_occupied_middles_by_symbol(Choice.EMPTY) * (-10)
        score = score + self.board.count_occupied_middles_by_symbol(Choice.CROSS) * (-30)

        if self.end_before_rotate:
            score = -100
            return score
        if self.check_lose():
            score = -200
            return score
        if self.check_win():
            score = 180
            return score
        print(score)
        return score

    @staticmethod
    def win_combinations():
        return [
        # horizontal -
        [(0,0,0), (0,0,1), (0,0,2), (1,0,0), (1,0,1)],
        [(0,0,1), (0,0,2), (1,0,0), (1,0,1), (1,0,2)],
        [(0,1,0), (0,1,1), (0,1,2), (1,1,0), (1,1,1)],
        [(0,1,1), (0,1,2), (1,1,0), (1,1,1), (1,1,2)],
        [(0,2,0), (0,2,1), (0,2,2), (1,2,0), (1,2,1)],
        [(0,2,1), (0,2,2), (1,2,0), (1,2,1), (1,2,2)],
        [(2,0,0), (2,0,1), (2,0,2), (3,0,0), (3,0,1)],
        [(2,0,1), (2,0,2), (3,0,0), (3,0,1), (3,0,2)],
        [(2,1,0), (2,1,1), (2,1,2), (3,1,0), (3,1,1)],
        [(2,1,1), (2,1,2), (3,1,0), (3,1,1), (3,1,2)],
        [(2,2,0), (2,2,1), (2,2,2), (3,2,0), (3,2,1)],
        [(2,2,1), (2,2,2), (3,2,0), (3,2,1), (3,2,2)],
        # vertical |
        [(0,0,0), (0,1,0), (0,2,0), (2,0,0), (2,1,0)],
        [(0,1,0), (0,2,0), (2,0,0), (2,1,0), (2,2,0)],
        [(0,0,1), (0,1,1), (0,2,1), (2,0,1), (2,1,1)],
        [(0,1,1), (0,2,1), (2,0,1), (2,1,1), (2,2,1)],
        [(0,0,2), (0,1,2), (0,2,2), (2,0,2), (2,1,2)],
        [(0,1,2), (0,2,2), (2,0,2), (2,1,2), (2,2,2)],
        [(1,0,0), (1,1,0), (1,2,0), (3,0,0), (3,1,0)],
        [(1,1,0), (1,2,0), (3,0,0), (3,1,0), (3,2,0)],
        [(1,0,1), (1,1,1), (1,2,1), (3,0,1), (3,1,1)],
        [(1,1,1), (1,2,1), (3,0,1), (3,1,1), (3,2,1)],
        [(1,0,2), (1,1,2), (1,2,2), (3,0,2), (3,1,2)],
        [(1,1,2), (1,2,2), (3,0,2), (3,1,2), (3,2,2)],
        # diagonal \
        [(0,0,0), (0,1,1), (0,2,2), (3,0,0), (3,1,1)],
        [(0,1,1), (0,2,2), (3,0,0), (3,1,1), (3,2,2)],
        [(0,0,1), (0,1,2), (1,2,0), (3,0,1), (3,1,2)],
        [(0,1,0), (0,2,1), (2,0,2), (3,1,0), (3,2,1)],
        # diagonal /
        [(1,0,2), (1,1,1), (1,2,0), (2,0,2), (2,1,1)],
        [(1,1,1), (1,2,0), (2,0,2), (2,1,1), (2,2,0)],
        [(1,0,1), (1,1,0), (0,2,2), (2,0,1), (2,1,0)],
        [(1,1,2), (1,2,1), (3,0,0), (2,1,2), (2,2,1)]
        ]

    @staticmethod
    def get_player_symbol(player_num):
        if player_num == 1:
            return Choice.CROSS
        else:
            return Choice.CIRCLE



algo = Negamax(2, win_score=150)
game = Pentago([Human_Player(), AI_Player(algo)])
game.play()
