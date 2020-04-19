import abc
from typing import Dict, List, Optional, Tuple
import logging
import random
from enum import Enum

from .move import Move
from .board import Board

class Viper(abc.ABC):
    """An abstract viper
    """
    COLORS = [
        '000000', # Black
        'FDDA24', # Yellow
        'EF3340'    # Red
    ]

    # Tail types for vipers
    class TailType(Enum):
        REGULAR = 'regular'
        BLOCK_BUM = 'block-bum'
        BOLT = 'bolt'
        CURLED = 'curled'
        FAT_RATTLE = 'fat-rattle'
        FRECKLED = 'freckled'
        HOOK = 'hook'
        PIXEL = 'pixel'
        ROUND_BUM = 'round_bum'
        SHARP = 'sharp'
        SKINYY = 'skinny'
        SMALL_RATTLE = 'small_rattle'
        BWC_BONHOMME = 'bwc-bonhomme'
        BWC_FLAKE = 'bwc-flake'
        BWC_ICE_SKATE = 'bwc_ice_skate'
        BWC_PRESENT = 'bwc_present'

    class HeadType(Enum):
        REGULAR = 'regular'
        BELUGA = 'beluga'
        BENDR = 'bendr'
        DEAD = 'dead'
        EVIL = 'evil'
        FANG = 'fang'
        PIXEL = 'pixel'
        SAFE = 'safe'
        SAND_WORM = 'sand-worm'
        SHADES = 'shades'
        SILLY  = 'silly'
        SMILE = 'smile'
        TONGUE = 'tongue'
        BWC_BONHOMME = 'bwc-bonhomme'
        BWC_EARMUFFS = 'bwc-earmuffs'
        BWC_RUDOLPH = 'bwc-rudolph'
        BWC_SCARF = 'bwc-scarf'
        BWC_SKI = 'bwc-ski'
        BWC_SNOW_WORM = 'bwc-snow-worm'
        BWC_SNOWMAN = 'bwc-snowman'

    viper_id: int
    name: str 
    health: int
    body: List
    shout: str

    def __init__(self, viper_id: int, name: str, health: int, body: List, shout: str):
        self.viper_id = viper_id,
        self.name = name
        self.health = health
        self.body = body
        self.shout = shout
        self.color = random.choice(Viper.COLORS)

    def __str__(self):
        return f'Viper with name {self.name} and color: ${self.color}.'

    ####################
    # Abstract methods #
    ####################

    @property
    @abc.abstractmethod
    def head(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def tail(self) -> str:
        pass

    @abc.abstractmethod
    def move(self, **kwargs) -> Move:
        pass

    ###################
    # General methods #
    ###################

    def get_config(self) -> Dict:
        return {
            'color': self.color,
            'headType': self.head,
            'tailType': self.tail
        }

    def determine_next_position(self, current_position: Dict, move: Move):

        if (move is Move.UP):
            new_position: Dict = self.determine_up_position(current_position)
        elif (move is Move.RIGHT):
            new_position: Dict = self.determine_right_position(current_position)
        elif (move is Move.DOWN):
            new_position: Dict = self.determine_down_position(current_position)
        else:
            new_position: Dict = self.determine_left_position(current_position)

        return new_position

    def determine_up_position(self, current_position: Dict) -> Dict:

        return {
            'x': current_position['x'],
            'y': (current_position['y'] - 1)
        }
    
    def determine_down_position(self, current_position: Dict) -> Dict:
        
        return {
            'x': current_position['x'],
            'y': (current_position['y'] + 1)
        }
    
    def determine_left_position(self, current_position: Dict) -> Dict:

        return {
            'x': (current_position['x'] - 1),
            'y': current_position['y']
        }

    def determine_right_position(self, current_position: Dict) -> Dict:

        return {
            'x': (current_position['x'] + 1),
            'y': current_position['y']
        }

    def determine_valid_moves(self, board: Board, viper_body: List) -> List[Move]:

        logging.info('Determining valid moves...')
        
        # Current position is the first element in the viper body List
        current_position: Dict = viper_body[0]
        logging.debug(f'Viper current position {current_position}')

        up_position: Dict = self.determine_up_position(current_position)
        down_position: Dict = self.determine_down_position(current_position)
        left_position: Dict = self.determine_left_position(current_position)
        right_position: Dict = self.determine_right_position(current_position)

        logging.debug(f'Next UP position {up_position}')
        logging.debug(f'Next DOWN position {down_position}')
        logging.debug(f'Next LEFT position {left_position}')
        logging.debug(f'Next RIGHT position {right_position}')

        moves: List = [
            (Move.UP, up_position),
            (Move.DOWN, down_position),
            (Move.LEFT, left_position),
            (Move.RIGHT, right_position)
        ]

        valid_moves = [move[0] for move in moves if not (board.is_occupied(move[1]) or board.is_out_of_bounds(move[1]))]

        return valid_moves