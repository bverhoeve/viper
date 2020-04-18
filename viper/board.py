from typing import List, Dict

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

        occupied_tiles = []
        
        # Any tile occupied by another snake is marked as occupied
        for snake in boardDict['snakes']:
            occupied_tiles.append(snake['body'])

        return occupied_tiles

    def update_food_tiles(self, boardDict: Dict) -> List:
        return boardDict['food']

    def update_tiles(self, boardDict: Dict) -> None:
        self.occupied_tiles = self.update_occupied_tiles(boardDict)
        self.food_tiles = self.update_food_tiles(boardDict)