import random

from .viper import Viper

class RandomViper(Viper):

    @property
    def head(self) -> str:
        return 'silly'

    @property
    def tail(self) -> str:
        return 'freckled'

    def move(self) -> str:
        return random.choice(Viper.MOVES)