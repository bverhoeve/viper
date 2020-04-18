import random

from .viper import Viper
from .move import Move

class RandomViper(Viper):

    @property
    def head(self) -> str:
        return 'silly'

    @property
    def tail(self) -> str:
        return 'freckled'

    def move(self) -> Move:
        return random.choice(list(Move))