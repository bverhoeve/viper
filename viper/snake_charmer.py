from typing import Dict

class SnakeCharmer:
  """SnakeCharmer class
  Manages the different games (snakes)
  """
  _games: Dict

  def __init__(self):
    # Initialize a games dictionary
    self._games = {}

  def start_game(self, game_data: Dict):
    pass
