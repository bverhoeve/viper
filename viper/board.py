from typing import List, Dict
import logging
import numpy as np

class Board:

    width: int
    height: int
    occupied_tiles: List
    food_tiles: List

    def __init__(self, boardDict: Dict) -> None:

        self.width = boardDict['width']
        self.height = boardDict['height']
        self.occupied_tiles = self.update_occupied_tiles(boardDict)
        self.food_tiles = self.update_food_tiles(boardDict)

    def update_occupied_tiles(self, boardDict: Dict) -> List:
  
        # Any tile occupied by another snake is marked as occupied
        occupied_tiles = [coordinate for snake in boardDict['snakes'] for coordinate in snake['body']]

        return occupied_tiles

    def update_food_tiles(self, boardDict: Dict) -> List:
        return boardDict['food']

    def update_tiles(self, boardDict: Dict) -> object:
        self.occupied_tiles = self.update_occupied_tiles(boardDict)
        self.food_tiles = self.update_food_tiles(boardDict)

        return self

    def is_occupied(self, position: Dict) -> bool:
        occupied: bool = position in self.occupied_tiles
        logging.debug(f'Occupied tiles {self.occupied_tiles}')
        logging.debug(f'Position {position} is occupied: {occupied}')
        return occupied

    def is_out_of_bounds(self, position: Dict) -> bool:
        out_of_bounds_x: bool = (0 > position['x']) or (position['x'] >= self.width)
        out_of_bounds_y: bool = (0 > position['y']) or (position['y'] >= self.height)

        out_of_bounds: bool = out_of_bounds_x or out_of_bounds_y
        logging.debug(f'Position {position} is out of bounds: {out_of_bounds}')

        return out_of_bounds_x or out_of_bounds_y

    def get_matrix_representation(self):
        """
        Get a matrix representation of the board
       
        matrix representation is 3 dimensions:
        - width of the board
        - height of the board
        - 2 values (free, food) where for
            - free: 0 is an occupied position, 1 is a free position
            - food: 0 is a food rich, 1 is foodless position

        Returns:
            [type] -- [description]
        """
        
        matrix = np.ones( (self.width, self.height, 2) )

        for position in self.occupied_tiles:
            matrix.itemset((position['x'], position['y'], 0), 0)
        for position in self.food_tiles:
            matrix.itemset((position['x'], position['y'], 1), 0)

        return matrix
