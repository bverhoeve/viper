import logging

from typing import Dict
from .random_viper import RandomViper, RandomCDViper
from .euclid_viper import EuclidViper
from .viper import Viper
from .move import Move
from .board import Board

class Game:
    """A game of snake
    """
    game_id: int
    turn: int
    board: Board
    viper: Viper

    def __init__(self, game_id: int, turn: int, boardDict: Dict, viperDict: Dict):
        self.game_id = game_id
        self.turn = turn
        self.board = Board(boardDict)

        shout = viperDict['shout'] if 'shout' in viperDict else ''

        self.viper = EuclidViper(
            viperDict['id'], viperDict['name'], viperDict['health'],
            viperDict['body'], shout
        )
    
    def get_viper(self):
        return self.viper

    def move(self, boardDict: Dict, viperDict: Dict):

        # Update board first
        self.board = self.board.update_tiles(boardDict)

        logging.debug(f'Current position of viper is {viperDict}')

        move: Move = self.viper.move(board=self.board, viper_body=viperDict['body'])

        move_response: Dict = {
            'move': move.value,
            'shout': self.viper.shout
        }

        return move_response