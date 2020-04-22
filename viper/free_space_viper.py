from scipy.spatial.distance import euclidean, cdist
import numpy as np
from typing import List, Dict, Tuple
import random
import logging

from .viper import Viper
from .board import Board
from .move import Move

class FreeSpaceViper(Viper):

    @property
    def head(self) -> str:
        return Viper.HeadType.BENDR.value

    @property
    def tail(self) -> str:
        return Viper.TailType.PIXEL.value

    def move(self, board: Board, viper_body: List) -> Move:    
        # Determine the valid moves
        valid_moves: List[Move] = self.determine_valid_moves(board, viper_body)

        return self.__determine_random_move(
            valid_moves
        )

    def __determine_random_move(self, valid_moves):
        return random.choice(valid_moves)


    def __find_free_spaces(self, board: Board):
        """
        Find the largest free space on the board
        """
        occupancy_matrix: np.ndarray = board.get_occupancy_matrix()
        logging.debug(f'The occupancy matrix is {occupancy_matrix}')
        auxiliary_matrix: np.ndarray = np.zeros([board.width, board.height])

        auxiliary_matrix[0, :] = occupancy_matrix[0, :, 0]
        auxiliary_matrix[:, 0] = occupancy_matrix[:, 0, 0]

        logging.debug(f'Building auxiliary matrix...')
        for i in range(1, board.width):
            for j in range(1, board.height):
                # A one in the first position indicates a free spot
                if (occupancy_matrix[i, j, 0] == 1):
                    auxiliary_matrix[i, j, 0] = min (
                        auxiliary_matrix[i, j-1, 0],
                        auxiliary_matrix[i-1, j ,0],
                        auxiliary_matrix[i-1, j-1, 0]
                        ) + 1

        logging.debug(f'Auxiliary matrix: {auxiliary_matrix}')
        
        return auxiliary_matrix
        
        