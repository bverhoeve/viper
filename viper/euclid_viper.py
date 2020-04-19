from scipy.spatial.distance import euclidean, cdist
import numpy
from typing import List, Dict
import random
import logging

from .viper import Viper
from .board import Board
from .move import Move

class EuclidViper(Viper):

    @property
    def head(self) -> str:
        return Viper.HeadType.BELUGA.value

    @property
    def tail(self) -> str:
        return Viper.TailType.BOLT.value

    def move(self, board: Board, viper_body: List) -> Move:
        
        # Determine the valid moves
        valid_moves: List[Move] = self.determine_valid_moves(board, viper_body)

        logging.debug(f'The valid moves are: {valid_moves}')

        current_position = viper_body[0]
        closest_food = self.__find_closest_food(current_position, board)
        logging.debug(f'Closest food is: {closest_food}')

        # Calculate closest food direction
        return random.choice(valid_moves)

    # def __determine_optimal_move(
    #   self, current_position: Dict, food_position: Dict, valid_moves: List) -> Move:
    # food_is_right: boolean = closest_food['x'] > current_position['x']
    # food_is_up: boolean = closest_food['y'] > current_position['y']
      #  if (food_is_right):
      # if (Move.RIGHT in valid_moves):
        # return Move.RIGHT
        # elif (food_is_up and Move.UP in valid_moves):
        # return Move.UP
        # elif (food_is_rig and Move.RIGHT in valid_moves):

    def __determine_random_move(self)

    def __find_closest_food(self, current_position: Dict, board: Board) -> Dict:
        # Brecht weet een betere methode, joepie!
        food_coordinates = [(food_tile['x'], food_tile['y']) for food_tile in board.food_tiles]
        current_position_coordinates = [(current_position['x'], current_position['y'])]
        # coordinates = current_position_coordinates + food_coordinates
        
        logging.debug(f'Current position coordinates: {current_position_coordinates}')
        logging.debug(f'Food coordinates: {food_coordinates}')
        
        # Maybe remove euclidian hardcoded arg in future
        distance_matrix = cdist(current_position_coordinates, food_coordinates, 'euclidean')
        logging.debug(f'Distance_matrix{distance_matrix}')
        
        distance_row: numpy.ndarray = distance_matrix[0]

        shortest_distance_index = distance_row.argmin()
        
        return board.food_tiles[shortest_distance_index]
