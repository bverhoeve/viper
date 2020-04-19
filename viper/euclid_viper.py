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
        return self.__determine_optimal_move(
            current_position,
            closest_food,
            valid_moves
        )
        
    def __determine_optimal_move(
        self, 
        current_position: Dict, 
        closest_food: Dict, 
        valid_moves: List
        ) -> Move:

        # Idea is to calculate the distance to the food and then calculate the new distances
        # for the position the snake will be in after it has made a move. The move that most 
        # greatly reduces the distance is the move that is the best move. If moves have 
        # the same reduction in distance, just pick a random one.

        # Not sure if needed yet
        current_distance: float = self.__determine_distance_to_food(current_position, closest_food)
        
        next_positions: List[Dict] = [self.determine_next_position(current_position, move) for move in valid_moves]
        next_distances: numpy.ndarray = numpy.array(
            [self.__determine_distance_to_food(new_position, closest_food) for new_position in next_positions]
        )

        next_info: str = ''
        for i in range(len(next_positions)):
            next_info: str = next_info + "position: " + str(next_positions[i]) + ", distance: " + str(next_distances[i]) + " | "
        logging.debug("Next possible positions: ")
        logging.debug(next_info)

        min_distance_index: int = next_distances.argmin()

        min_move: Move = valid_moves[min_distance_index]

        logging.debug(f'Minimal move found is {min_move}')
        
        return min_move

    def __determine_random_move(self, valid_moves):
        return random.choice(valid_moves)

    def __determine_distance_to_food(self, current_position: Dict, food_position: Dict):
        return euclidean(
            [current_position['x'], current_position['y']],
            [food_position['x'], food_position['y']]
        )

    def __find_closest_food(self, current_position: Dict, board: Board) -> Dict:
        
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
