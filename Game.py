import Boards

__author__ = 'TESR'

from Boards import Board

class Game(object):
    turn = 'W'
    gameEnded = False
    count = 0                   # number of steps made
    fiftyCount = 0              # no of steps made without moving a pawn or killing

    b = Board.Board()

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
            #g.gameEnded = True   #Just stopping the game
        return g

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

def main():
    g = Game()
    g.printBoard()
    while(not g.gameEnded):
        g = g.playGame()


if __name__ == '__main__':
    main()
