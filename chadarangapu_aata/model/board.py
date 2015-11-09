__author__ = 'TESR'

from piece import *

import logging
_logger = logging.getLogger(__name__)

class Board(object):

    def __init__(self):
        '''
        Material            :   A list of all piece objects on the board
        Piece_Dictionary    :   Every piece on the board has an entry in this dictionary (Eg: {"11" : Rook_obj} for a Rook at (1,1)
        '''
        _logger.debug("Initializing board")
        self.material = []
        self.piece_dictionary = dict()
        self.initialize_board()

    def place_piece(self, piece_obj):
        '''
        Append the newly placed piece to the material list of the board
        Create an entry for the newly placed piece in the piece dictionary
        '''
        self.material.append(piece_obj)
        piece_key = str(piece_obj.x) + str(piece_obj.y)
        self.piece_dictionary[piece_key] = piece_obj
        _logger.debug("Placed piece: %s"%(piece_obj.name))

    def remove_piece(self, source_x, source_y):
        '''
        Removing the piece from the board's material list
        Removing the key in the piece_dictionary
        '''
        piece_identifier = str(source_x)+str(source_y)
        removed_piece = self.piece_dictionary[piece_identifier]
        # Removed piece from material list
        self.material.remove(removed_piece)
        # Updating piece_dictionary
        del self.piece_dictionary[piece_identifier]

        _logger.debug("Removed piece:%s from the square: %s,%s and returning the piece object" %(removed_piece.name,source_x, source_y))
        return removed_piece

    def initialize_board(self):
        '''
        This method declares the initial material/ pieces to be placed on the board
        Then it adds all the material to the board's material list by calling place_piece() function
        '''
        initial_material = [
            Rook('W',1,1), Rook('W',1,8),
            Rook('B',8,1), Rook('B',8,8),

            Knight('W',1,2), Knight('W',1,7),
            Knight('B',8,2), Knight('B',8,7),

            Bishop('W',1,3), Bishop('W',1,6),
            Bishop('B',8,3), Bishop('B',8,6),

            King('W',1,5), King('B',8,5),
            Queen('W',1,4), Queen('B',8,4),

            Pawn('W',2,1), Pawn('W',2,2), Pawn('W',2,3), Pawn('W',2,4), Pawn('W',2,5), Pawn('W',2,6), Pawn('W',2,7), Pawn('W',2,8),
            Pawn('B',7,1), Pawn('B',7,2), Pawn('B',7,3), Pawn('B',7,4), Pawn('B',7,5), Pawn('B',7,6), Pawn('B',7,7), Pawn('B',7,8)
        ]
        _logger.debug("Populating the initial board with pieces")

        for piece_obj in initial_material:
            self.place_piece(piece_obj)


    def update_board(self, source1, source2, dest1, dest2):
        '''
        When a move of format (source_x,source_y, dest_x, dest_y) is given to this function, it does the following
        1) removes the piece from (source_x, source_y)
        2) place the removed piece in (dest_x, dest_y)
        '''
        piece_obj = self.remove_piece(source1, source2)
        piece_obj.x, piece_obj.y = dest1, dest2
        self.place_piece(piece_obj)

        _logger.info("Updated the board")


    def __str__(self):
        '''
        This function is the string representation the chess board. can be called using python print function
        '''

        WHITE = '\033[89m'
        BLACK = '\033[91m'
        ENDC = '\033[0m'

        chess_board_footer = '''\
***********************
  - A B C D E F G H -
'''
        chess_board_str = ""

        # Scanning from (1,1) to (8,8) searching for pieces in piece_dictionary
        for i in range(8,0, -1):
            chess_board_str+= "%s |" %(i)
            for y in range(1,9):
                current_sqr_identifier = str(i)+str(y)
                piece = self.piece_dictionary.get(current_sqr_identifier)
                if piece:
                    if piece.colour == "W":
                        chess_board_str += " "+WHITE+piece.representation+ENDC

                    elif piece.colour == "B":
                        chess_board_str += " "+BLACK+piece.representation+ENDC
                else:
                    chess_board_str+= "  "
            chess_board_str+="\n"

        chess_board_str = chess_board_str + chess_board_footer

        return chess_board_str
