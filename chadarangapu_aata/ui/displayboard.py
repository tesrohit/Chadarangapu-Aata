__author__ = 'Ayodhya'

import logging

_logger = logging.getLogger(__name__)


def print_board(board_obj):
    '''
    This function can be changed according to the changing board object
    :param board_obj:
    :return:
    '''
    print "  ",
    for x in range(65, 73):
        print chr(x) + " ",
    print ""
    index = 0
    for x in board_obj.ChessBoard:
        index += 1
        print index,
        for y in x:
            print(y.name[0] + y.colour[0]),
        print (8 - index + 1)
    print "  ",
    for x in range(65, 73):
        print chr(x) + " ",
    print ""
