from board import Board
from choice import Choice

class Pentago():

    def __init__(self):
        self.board = Board()
        self.current_choice = Choice.CROSS
    
    def make_move(self):
        print("Teraz ruch ma: " + self.current_choice.value)
        self.board.print_board()
        choice_placed = False
        while not choice_placed:
            quadrant = int(input("Jaka cwiartka sie dzisiaj zajmujemy byczku?: "))
            print("Daj wspolrzedne cwiartki: ")
            x = int(input("Kolumna: "))
            y = int(input("Rzad: "))
            choice_placed = self.board.place_choice(self.current_choice, quadrant, y, x)
            if not choice_placed:
                print("Nie no byczku juz tam cos jest, sprobuj jeszcze raz")
        self.board.print_board()
        direction = int(input("W ktora strone chcesz obrocic cwiartke (lewo - 0, prawo - 1)?: "))
        self.board.rotate_quadrant(quadrant, direction)
        if self.current_choice == Choice.CROSS:
            self.current_choice = Choice.CIRCLE
        else:
            self.current_choice = Choice.CROSS

game = Pentago()
while(True):
    game.make_move()