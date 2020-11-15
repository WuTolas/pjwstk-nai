from board import Board
from choice import Choice
from easyAI import TwoPlayersGame, Negamax, Human_Player, AI_Player


class Pentago(TwoPlayersGame):

    def __init__(self, players):
        self.board = Board()
        self.players = players
        self.nplayer = 1

    def make_move(self, move):
        quadrant_before, x, y, quadrant_after, rotate = move
        player_symbol = self.get_player_symbol(self.nplayer)
        self.board.place_choice(player_symbol, quadrant_before - 1, y - 1, x - 1)
        self.board.rotate_quadrant(quadrant_after - 1, rotate - 1)

    def unmake_move(self, move):
        quadrant_before, x, y, quadrant_after, rotate = move
        player_symbol = Choice.EMPTY
        if rotate == 1:
            rotate = 2
        else:
            rotate = 1
        self.board.rotate_quadrant(quadrant_after - 1, rotate - 1)
        self.board.place_choice(player_symbol, quadrant_before - 1, y - 1, x - 1)

    def lose(self):
        #TODO
        pass

    def possible_moves(self):
        return self.board.available_moves()

    def show(self):
        self.board.print_board()

    def is_over(self):
        return (self.possible_moves() == []) or self.lose()

    def scoring(self):
        return -200 if self.lose() else 0

    @staticmethod
    def win_combinations():
        #TODO
        return []

    @staticmethod
    def get_player_symbol(player_num):
        if player_num == 1:
            return Choice.CROSS
        else:
            return Choice.CIRCLE


algo = Negamax(10)
game = Pentago([Human_Player(), AI_Player(algo)])
game.play()
