import logging

from typing import Dict
from viper import Snake

class Game:
    """A game of snake
    """
    game_id: int
    turn: int
    board: Dict

    # To implement
    snake: object

    def __init__(self, game_id: int, turn: int, board: Dict, our_snake: Dict):
        self.game_id = game_id
        self.turn = turn
        self.board = board
    