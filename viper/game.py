import logging

from typing import Dict
from .random_viper import RandomViper
from .viper import Viper

class Game:
    """A game of snake
    """
    game_id: int
    turn: int
    board: Dict
    viper: Viper

    def __init__(self, game_id: int, turn: int, board: Dict, viperDict: Dict):
        self.game_id = game_id
        self.turn = turn
        self.board = board
        self.viper = RandomViper(
            viperDict['id'], viperDict['name'], viperDict['health'],
            viperDict['body'], viperDict['shout']
        )
    
    def get_viper(self):
        return self.viper

    def move(self):
        move: str = self.viper.move()

        move_response: Dict = {
            'move': move,
            'shout': self.viper.shout
        }

        return move_response