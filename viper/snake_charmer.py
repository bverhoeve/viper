import logging

from typing import Dict
from .game import Game
from .viper import Viper

class SnakeCharmer:
    """SnakeCharmer class
    Manages the different games (snakes)
    """
    __instance = None
    __games: Dict[int, Game] = {}

    def __new__(cls):

        if SnakeCharmer.__instance is None:
            logging.debug('Creating new SnakeCharmer')
            SnakeCharmer.__instance = object.__new__(cls)
            SnakeCharmer.__instance._games = {}
            
        return SnakeCharmer.__instance

    def get_numer_of_active_games(self):
        return len(self.__games)

    def end_game(self, game_id):
        self.__games[game_id] = None

    def start_game(self, game_id: int, turn: int, board: Dict, viperDict: Dict) -> Viper:
        new_game = Game(game_id, turn, board, viperDict)
        self.__games[game_id] = new_game
        return new_game.get_viper()

    def move(self, game_id: int, turn: int, board: Dict, viperDict: Dict):
        logging.debug(f'Making a move in game with id {game_id}')
        game: Game = self.__games[game_id]
        move_response = game.move()

        return move_response
