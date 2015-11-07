__author__ = 'TESR'
'''
Main script which starts and maintains the game
'''

import logging
import chadarangapu_aata.commons as commons

from chadarangapu_aata.model import Board
from chadarangapu_aata.ui import print_board, get_user_move
from chadarangapu_aata.engine import check_valid_move

_logger = logging.getLogger()

class Game(object):
    def __init__(self, player_white="TestWhite", player_black="TestBlack"):

        """


        :rtype : object
        :type player_white: str
        :type player_black: str
        """
        _logger.debug("Initializing game object")
        self.players = dict()
        self.players["W"] = player_white
        self.players["B"] = player_black
        self.board = Board()

        # Initiating all other game parameters
        if not (player_black == "CPU" or player_white == "CPU"):    # Tokkalo logic
            self.type = "2player"

        self.turn = 'W'
        self.game_ended = False
        self.fifty_count = False  # no of steps made without moving a pawn or killing

        _logger.debug("Initialized game object: %s" %(locals()))

def two_player_game(curr_game):

    while not curr_game.game_ended:
        # Try to get user_input from the user regarding the move.
        # The below function only performs basic checks regarding the move
        if curr_game.turn == "W":
            _logger.info("White's turn:")
        elif curr_game.turn == "B":
            _logger.info("Black's turn:")

        move = get_user_move()

        if move:
            # If the move is specified, check for its validity

            if check_valid_move(move, curr_game.turn, curr_game.board):
                _logger.debug("the move: %s is valid" %(move))

                # Updating the game's board object with new changes
                # BOARD.PY NAKU NACHALE
                #curr_game.board.update_board()

                # Toggling turn for white and black
                curr_game.turn = "B" if curr_game.turn == "W" else "W"

                # Calling the UI to display updated board
                print_board(curr_game.board)

            else:
                _logger.info("Invalid move!")
                _logger.debug("Continue asking for same move")
                continue

def main():

    # Configuring logging at info level... set environment variable to override "set AATA_LOG_LEVEL=DEBUG"
    commons.configure_logging(_logger)

    # You can include the logic for asking the player names here.. ignoring for now
    curr_game = Game()

    _logger.info("Initial board...")
    print_board(curr_game.board)

    if curr_game.type == "2player":
        _logger.info("Starting a two player game")
        two_player_game(curr_game)



if __name__ == '__main__':
    main()