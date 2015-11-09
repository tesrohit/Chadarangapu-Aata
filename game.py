__author__ = 'TESR'
'''
Main script which starts and maintains the game
'''

import logging
import chadarangapu_aata.commons as commons

from chadarangapu_aata.model import *
from chadarangapu_aata.ui import print_board, get_user_move
from chadarangapu_aata.engine import check_valid_move


_logger = logging.getLogger()

class Game(object):
    def __init__(self, player_white="TestWhite", player_black="TestBlack",game_type="2player"):

        self.players = {
            "WHITE": player_white,
            "BLACK": player_black
        }
        self.board = Board()

        # Initiating all other game parameters

        self.type = game_type
        self.turn = 'W'
        self.game_result = 100
        self.fifty_count = False  # no of steps made without moving a pawn or killing

        _logger.debug("Initialized game object: %s" %(locals()))

    def start_two_player_game(self):
        '''
        This method starts a two player game
        '''

        _logger.info("Starting a two player game")

        while self.game_result == 100:
            if self.turn == "W":
                print("White's turn:")
            elif self.turn == "B":
                print("Black's turn:")

            move = get_user_move()

            if move:
                if check_valid_move(move, self.turn, self.board):
                    _logger.debug("The move %s is valid" %str(move))

                    # Updating the game's board object with new changes
                    self.board.update_board(*move)

                    # Toggling turn for white and black
                    self.turn = "B" if self.turn == "W" else "W"

                    # Calling the UI to display updated board
                    print self.board

                else:
                    _logger.info("Invalid move!")
                    continue

def main():

    # set environment variable AATA_LOG_LEVEL to change log level (currently INFO)
    commons.configure_logging(_logger)

    curr_game = Game()

    if curr_game.type == "2player":
        curr_game.start_two_player_game()

    if curr_game.game_result == 0:
        print("TIED GAME")
    elif curr_games.game_result == 1:
        print("PLAYER-WHITE WON")
    else:
        print("PLAYER-BLACK WON")

if __name__ == '__main__':
    main()