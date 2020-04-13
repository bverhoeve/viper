import logging

from typing import Dict

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

  def start_game(self, game_data: Dict):
    pass
