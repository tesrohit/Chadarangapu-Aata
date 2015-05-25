__author__ = 'TESR-PVPK'

# B - Black Piece
# W - White Piece
# Z - Colour given to the blank places
# R - Rook pieces in the board
# N - Knight pieces in the board
# B - Bishop pieces in the board
# K - King pieces in the board
# Q - Queen pieces in the board
# P - Pawn pieces in the board
# bk - Blank Places in the board


class Piece(object):  # Abstract Class for every piece
    def move(self, dest1, dest2):
        pass


class Rook(Piece):
    def __init__(self, colour):
        self.name = 'Rook'
        self.colour = colour

    def move(self, dest1, dest2):
        """Implementing the logic"""


class Knight(Piece):
    def __init__(self, colour):
        self.name = 'Knight'
        self.colour = colour

    def move(self, dest1, dest2):
        """Implementing the logic"""


class Bishop(Piece):
    def __init__(self, colour):
        self.name = 'Bishop'
        self.colour = colour

    def move(self, dest1, dest2):
        """Implementing the logic"""


class King(Piece):
    def __init__(self, colour):
        self.name = 'King'
        self.colour = colour

    def move(self, dest1, dest2):
        """Implementing the logic"""


class Queen(Piece):
    def __init__(self, colour):
        self.name = 'Queen'
        self.colour = colour

    def move(self, dest1, dest2):
        """Implementing the logic"""


class Pawn(Piece):
    def __init__(self, colour):
        self.name = 'Pawn'
        self.colour = colour

    def move(self, dest1, dest2):
        """Implementing the logic"""


class Blank(Piece):
    def __init__(self, colour):
        self.name = 'Empty'
        self.colour = colour

    def move(self, dest1, dest2):
        """Implementing the logic"""
        print "Invalid Position"
        return


class Board(object):
    R1 = Rook('W')
    R2 = Rook('W')
    r1 = Rook('B')
    r2 = Rook('B')

    N1 = Knight('W')
    N2 = Knight('W')
    n1 = Knight('B')
    n2 = Knight('B')

    B1 = Bishop('W')
    B2 = Bishop('W')
    b1 = Bishop('B')
    b2 = Bishop('B')

    K1 = King('W')
    k1 = King('B')

    Q1 = Queen('W')
    q1 = Queen('B')

    P1 = Pawn('W')
    P2 = Pawn('W')
    P3 = Pawn('W')
    P4 = Pawn('W')
    P5 = Pawn('W')
    P6 = Pawn('W')
    P7 = Pawn('W')
    P8 = Pawn('W')

    p1 = Pawn('B')
    p2 = Pawn('B')
    p3 = Pawn('B')
    p4 = Pawn('B')
    p5 = Pawn('B')
    p6 = Pawn('B')
    p7 = Pawn('B')
    p8 = Pawn('B')

    bk = Blank('Z')

    ChessBoard = [[R1, N1, B1, Q1, K1, B2, N2, R2],
                  [P1, P2, P3, P4, P5, P6, P7, P8],
                  [bk, bk, bk, bk, bk, bk, bk, bk],
                  [bk, bk, bk, bk, bk, bk, bk, bk],
                  [bk, bk, bk, bk, bk, bk, bk, bk],
                  [bk, bk, bk, bk, bk, bk, bk, bk],
                  [p1, p2, p3, p4, p5, p6, p7, p8],
                  [r1, n1, b1, q1, k1, b2, n2, r2]]

    def human_move(self, move, turn):
        source1 = ord(move[0]) - 65
        source2 = int(move[1])
        dest1 = ord(move[2]) - 65
        dest2 = int(move[3])
        # print source1, source2
        # print self.ChessBoard[source2 - 1][source1].colour + " " + turn
        if self.ChessBoard[source2 - 1][source1].colour == turn:
            self.ChessBoard[source2 - 1][source1].move(dest2, dest1)
        else:
            print "Invalid Color"


class Game(object):
    turn = 'W'  # indicates the turn whether black or white
    b = Board()
    count = 0  # number of steps made
    fifty_count = 0  # no of steps made without moving a pawn or killing
    # print "00 ", b.ChessBoard[0][0].colour

    # ----------------- Printing Chess Board ----------------------#
    print " ",
    for x in range(65, 73):
        print chr(x),
    print ""
    index = 0
    for x in b.ChessBoard:
        index += 1
        print index,
        for y in x:
            print(y.name[0] + y.colour[0]),
        print (8 - index + 1)
    print " ",
    for x in range(65, 73):
        print chr(x),
    print ""
    # ----------------- Printing Chess Board ----------------------#

    move = raw_input('Enter the move(Source-Destination):')
    if len(move) != 4:
        print "Wrong input(Source - Destination)"
    else:
        b.human_move(move, turn)

        # print "00 ", b.ChessBoard[0][0].colour


def main():
    g = Game()


if __name__ == '__main__':
    main()