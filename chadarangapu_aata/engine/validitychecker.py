__author__ = 'Ayodhya'

import logging

_logger = logging.getLogger(__name__)

def check_valid_move(move, turn, board):
    '''
    Checks if a given move is valid in the current board position for the current turn
    :param move: tuple (x,y)
    :param board: board_obj
    :return: True for valid moves. False for invalid moves
    '''
    _logger.debug("Checking validity of move: %s, turn: %s, board: %s" %(move, turn, board))
    _logger.info("Returning true for all moves since currently under testing")
    return True
