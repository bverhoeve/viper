import abc
from typing import Dict
import logging
import random

class Viper(abc.ABC):
    """An abstract viper
    """
    COLORS = [
        '000000', # Black
        'FDDA24', # Yellow
        'EF3340'    # Red
    ]

    # Todo, check which head we want
    HEADS = [
        'regular',
    ]

    # 
    TAILS = [
        'regular'
    ]

    MOVES = [
        'up',
        'down',
        'left',
        'right'
    ]

    viper_id: int
    name: str 
    health: int
    body: Dict
    shout: str

    def __init__(self, viper_id: int, name: str, health: int, body: Dict, shout: str):
        self.viper_id = viper_id,
        self.name = name
        self.health = health
        self.body = body
        self.shout = shout
        self.color = random.choice(Viper.COLORS)

    @property
    @abc.abstractmethod
    def head(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def tail(self) -> str:
        pass

    def get_config(self) -> Dict:
        return {
            'color': self.color,
            'headType': self.head,
            'tailType': self.tail
        }

    @abc.abstractmethod
    def move(self):
        pass