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
    def move(self, source1, source2,  dest1, dest2):
        pass


class Rook(Piece):
    def __init__(self, colour):
        self.name = 'Rook'
        self.colour = colour

    def move(self, source1, source2, dest1, dest2):
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

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""


class King(Piece):
    def __init__(self, colour):
        self.name = 'King'
        self.colour = colour

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""


class Queen(Piece):
    def __init__(self, colour):
        self.name = 'Queen'
        self.colour = colour

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""


class Pawn(Piece):
    def __init__(self, colour):
        self.name = 'Pawn'
        self.colour = colour

    def move(self, source1, source2, dest1, dest2):
        result = False
        vertical = False
        horizontal = False
        print str(source1) + " " + str(source2) + " " + str(dest1) + " " + str(dest2)
        if source1 == 1:
            if dest1 == 2:
                vertical = True
            elif dest1 == 3:
                vertical = True
        else:
            if (dest1 - source1) == 1:
                vertical = True

        if source2 == dest2:
            horizontal = True

        if (horizontal and vertical):
            result = True
            return result
        return result
        """Implementing the logic"""


class Blank(Piece):
    def __init__(self, colour):
        self.name = 'Empty'
        self.colour = colour

    def move(self, source1, source2, dest1, dest2):
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

    def update_board(self,source1,source2,dest1,dest2):
        temp_pawn = Blank('Z')
        temp_pawn = self.ChessBoard[source1][source2]
        self.ChessBoard[source1][source2] = self.ChessBoard[dest1][dest2]
        self.ChessBoard[dest1][dest2] = temp_pawn
        return

    def human_move(self, move, turn):
        source2 = ord(move[0]) - 65
        source1 = int(move[1]) - 1
        dest2 = ord(move[2]) - 65
        dest1 = int(move[3]) - 1

        if turn == 'B':
            source1 = 8 - source1 - 1
            dest1 = 8 - dest1 - 1
        if self.ChessBoard[source1][source2].colour == turn:
            # print self.ChessBoard[source2][source1].name
            if(self.ChessBoard[source1][source2].move(source1, source2, dest1, dest2)):
                self.update_board(source1, source2, dest1, dest2)#Update board
                return
        else:
            print "You can only move pieces of your color"


class Game(object):
    turn = 'W'
    gameEnded = False
    count = 0                   # number of steps made
    fiftyCount = 0              # no of steps made without moving a pawn or killing

    b = Board()

    def getMove(self, turn):
        move = raw_input('Enter the move(Source-Destination Eg:"E2E4"):')
        if len(move) != 4:   #String should be size of 4 characters
            print "Wrong input(SourcePosition - DestinationPosition)"
            main()

        if ((ord(move[0]) not in range(ord('A'),ord('G')+1)) and (ord(move[2]) not in range(ord('A'),ord('G')+1))): #Checking the alphabets are given in range of [A,G]
            print "Give correct characters which indicate positions"
            main()

        if ((int(move[1]) not in range(0,9)) and (int(move[3]) not in range(0,9))): #Checking the numbers given in the range of [1,8]
            print "Give correct numbers which indicate positions"
            main()
        else:
            self.b.human_move(move, turn)

    def printBoard(self):
        print "  ",
        for x in range(65, 73):
            print chr(x) + " ",
        print ""
        index = 0
        for x in self.b.ChessBoard:
            index += 1
            print index,
            for y in x:
                print(y.name[0] + y.colour[0]),
            print (8 - index + 1)
        print "  ",
        for x in range(65, 73):
            print chr(x) + " ",
        print ""
    # ----------------- Printing Chess Board ----------------------#

    def playGame(self):
        g = self
        turn = g.turn

        # These three steps should be fundamental for every move
        g.getMove(turn)         # This function checks whose move it is and gets the move from human/computer
        #g.updateBoard()       # This function contains validity checks
        g.printBoard()          # This function prints the board as it is

        if(g.turn is 'W'):
            print "White's turn ended"
            g.turn = 'B'
        else:
            print "Black's turn ended"
            g.turn = 'W'
            g.gameEnded = True   #Just stopping the game
        return g

def main():
    g = Game()
    g.printBoard()
    while(not g.gameEnded):
        g = g.playGame()


if __name__ == '__main__':
    main()