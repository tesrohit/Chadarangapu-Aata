__author__ = 'TESR'

from Pieces import Piece

class Board(object):
    R1 = Piece.Rook('W')
    R2 = Piece.Rook('W')
    r1 = Piece.Rook('B')
    r2 = Piece.Rook('B')

    N1 = Piece.Knight('W')
    N2 = Piece.Knight('W')
    n1 = Piece.Knight('B')
    n2 = Piece.Knight('B')

    B1 = Piece.Bishop('W')
    B2 = Piece.Bishop('W')
    b1 = Piece.Bishop('B')
    b2 = Piece.Bishop('B')

    K1 = Piece.King('W')
    k1 = Piece.King('B')

    Q1 = Piece.Queen('W')
    q1 = Piece.Queen('B')

    P1 = Piece.Pawn('W')
    P2 = Piece.Pawn('W')
    P3 = Piece.Pawn('W')
    P4 = Piece.Pawn('W')
    P5 = Piece.Pawn('W')
    P6 = Piece.Pawn('W')
    P7 = Piece.Pawn('W')
    P8 = Piece.Pawn('W')

    p1 = Piece.Pawn('B')
    p2 = Piece.Pawn('B')
    p3 = Piece.Pawn('B')
    p4 = Piece.Pawn('B')
    p5 = Piece.Pawn('B')
    p6 = Piece.Pawn('B')
    p7 = Piece.Pawn('B')
    p8 = Piece.Pawn('B')

    bk = Piece.Blank('Z')

    ChessBoard = [[R1, N1, B1, Q1, K1, B2, N2, R2],
                  [P1, P2, P3, P4, P5, P6, P7, P8],
                  [bk, bk, bk, bk, bk, bk, bk, bk],
                  [bk, bk, bk, bk, bk, bk, bk, bk],
                  [bk, bk, bk, bk, bk, bk, bk, bk],
                  [bk, bk, bk, bk, bk, bk, bk, bk],
                  [p1, p2, p3, p4, p5, p6, p7, p8],
                  [r1, n1, b1, q1, k1, b2, n2, r2]]

    def update_board(self,source1,source2,dest1,dest2):
        temp_pawn = Piece.Blank('Z')
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
            if(self.ChessBoard[source1][source2].move(source1, source2, dest1, dest2)):
                self.update_board(source1, source2, dest1, dest2)#Update board
                return
        else:
            print "You can only move pieces of your color"
