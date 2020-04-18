import random
from typing import List
import logging

from .viper import Viper
from .move import Move
from .board import Board

class RandomViper(Viper):

    @property
    def head(self) -> str:
        return 'silly'

    @property
    def tail(self) -> str:
        return 'freckled'

    def move(self, **kwargs) -> Move:
        return random.choice(list(Move))

class RandomCDViper(Viper):

    @property
    def head(self) -> str:
        return 'silly'

    @property
    def tail(self) -> str:
        return 'freckled'

    def move(self, board: Board, viper_body: List) -> Move:
        
        # Determine the valid moves
        valid_moves: List[Move] = self.determine_valid_moves(board, viper_body)

        logging.debug(f'The valid moves are: {valid_moves}')

        # Choose a random move from the valid moves
        return random.choice(valid_moves)