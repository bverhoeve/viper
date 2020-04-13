import abc
from typing import Dict
import logging
import random

# Todo, make abstract class
class Snake():
    """An abstract snake
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

    snake_id: int
    name: str 
    health: int
    body: Dict
    shout: str
    color: str
    head: str
    tail: str

    def __init__(self, snake_id: int, name: str, health: int, body: Dict, shout: str):
        self.snake_id = snake_id,
        self.name = name
        self.health = health
        self.body = body
        self.shout = shout
        self.color = random.choice(Snake.COLORS)
        self.head = random.choice(Snake.HEADS)
        self.tail = random.choice(Snake.TAILS)

    @property
    def snake_config(self) -> Dict:
        return {
            'color': self.color,
            'headType': self.head,
            'tailType': self.tail
        }
    

    
