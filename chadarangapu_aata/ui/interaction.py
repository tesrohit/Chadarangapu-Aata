__author__ = 'Ayodhya'

import logging

_logger = logging.getLogger(__name__)

def get_user_move():
        move = raw_input('Enter the move(Source-Destination Eg:"E2E4"):')

        if len(move) != 4:  # String should be size of 4 characters
            print "Wrong input(SourcePosition - DestinationPosition)"
            return None

        if ((ord(move[0]) not in range(ord('A'), ord('G') + 1)) and (
            ord(move[2]) not in range(ord('A'), ord('G') + 1))):  # Checking the alphabets are given in range of [A,G]
            print "Give correct characters which indicate positions"
            return None

        if ((int(move[1]) not in range(0, 9)) and (
            int(move[3]) not in range(0, 9))):  # Checking the numbers given in the range of [1,8]
            print "Give correct numbers which indicate positions"
            return None

        return move
