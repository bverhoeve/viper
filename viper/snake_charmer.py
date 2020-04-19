import logging

from typing import Dict
from .game import Game
from .viper import Viper

class SnakeCharmer:
    """SnakeCharmer class
    Manages the different games (snakes)
    """
    __instance = None

    def __new__(cls):

        if SnakeCharmer.__instance is None:
            logging.debug('Creating new SnakeCharmer')
            SnakeCharmer.__instance = object.__new__(cls)
            SnakeCharmer.__instance._games = {}
            
        return SnakeCharmer.__instance
    
    # Deprecated
    # def get_numer_of_active_games(self):
      #  return len(self.__games)

    def end_game(self, game_id):
        # remove the game from some in memory storage
        pass

    def start_game(self, game_id: int, turn: int, board: Dict, viperDict: Dict) -> Viper:
        new_game = Game(game_id, turn, board, viperDict)
        # save the game in some in memory storage
        return new_game.get_viper()

    def move(self, game_id: int, turn: int, board: Dict, viperDict: Dict):
        logging.debug(f'Making a move in game with id {game_id}')
       #  game: Game = self.__games[game_id]
        game: Game = Game(game_id, turn, board, viperDict)
        move_response = game.move(board, viperDict)

        return move_response
