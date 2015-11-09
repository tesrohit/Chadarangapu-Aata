__author__ = 'Ayodhya'

import logging
from validitychecker import check_valid_move

_logger = logging.getLogger(__name__)

def make_move(turn, board):
    '''
    This function takes the input from the user based on the turn
    :param turn:
    :return:
    '''

    while True:     # Keep asking until you get a valid move
        move = get_user_move()
        if move:
            break

    # Check if the given move is valid for the given turn for a given board position
    is_valid = check_valid_move(move, turn, board)

    if is_valid:
        update_board(move)
        return True

    else:
        return None


def update_board(move):
    pass


def get_computer_move():
    '''
    Computer Move generator. For now only 2-player is supported
    :return: None
    '''
    return None



