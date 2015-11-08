__author__ = 'Ayodhya'

import logging

_logger = logging.getLogger(__name__)

class bcolors:

    WHITE = '\033[92m'
    BLACK = '\033[93m'
    ENDC = '\033[0m'



def print_board(board_obj):
    '''
    This function can be changed according to the changing board object
    :param board_obj:
    :return:
    '''

    WHITE = '\033[92m'
    BLACK = '\033[93m'
    ENDC = '\033[0m'

    chess_board = [[None for x in range(8)] for x in range(8)]

    for piece_key, piece_obj in board_obj.piece_dictionary.iteritems():
        piece_x, piece_y = int(piece_key[0]), int(piece_key[1])
        chess_board[piece_x-1][piece_y-1] = piece_obj


    print "  - A B C D E F G H - "
    print "  --------------------  "
    index = 0
    for row in range(0,8):
        index += 1
        print "%s |" %(index),
        for column in range(0,8):
            if chess_board[row][column]:
                piece = chess_board[row][column]
                if piece.colour == "B":
                    print BLACK+piece.representation+ENDC,

                elif piece.colour == "W":
                    print WHITE+piece.representation+ENDC,
            else:
                print " ",
        print "|"
    print "  -------------------  "
    print "  - A B C D E F G H - "

