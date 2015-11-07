__author__ = 'TESR'

'''
NAKU NACHALE:

1) class variables anni __init__ lo undali per instance

2)

3) ipudu kotta piece vachindi anuko.. lekapote piece chachipote ela?

   Ivi naku anipichina changes prastutaniki
     -- piece initial_position piece.py lo undali
     -- pieces declaration game lo undali (since pieces are for a game.. pawn queening, piece death etc..)
     -- board lo place_piece()/remove_piece() ani functions rasi pieces pettali/teeseyali (update_board lo kuda use avtundi)
'''


from piece import *

import logging
_logger = logging.getLogger(__name__)

class Board(object):
    _logger.debug("Initializing board")
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

    def update_board(self, source1, source2, dest1, dest2):
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
        # print source1, source2, dest1, dest2
        # print self.ChessBoard[source2][source1].colour + " " + turn
        if self.ChessBoard[source1][source2].colour == turn:
            # print self.ChessBoard[source2][source1].name
            if (self.ChessBoard[source1][source2].move(source1, source2, dest1, dest2)):
                self.update_board(source1, source2, dest1, dest2)  # Update board
                return
        else:
            print "You can only move pieces of your color"
