from enum import Enum

class Move(Enum):
    """Enum of available moves for a viper
    """
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    def __str__(self) -> str:
        return self.value