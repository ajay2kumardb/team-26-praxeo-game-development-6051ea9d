import logging
from dataclasses import dataclass
from enum import Enum
from levelup.map import GameMap
from levelup.character import Character


DEFAULT_CHARACTER_NAME = "Character"

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
#    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (-100,-100)
    move_count: int = 0

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:


    status: GameStatus

    def __init__(self):
        self.status = GameStatus()
        self.map = GameMap(100)

    def start_game(self):
        pass


    # Pre-implemented to demonstrate ATDD
    # TODO: Update this if it does not match your design (hint - it doesnt)
    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.character = Character(character_name)
            self.status.current_position = self.character.getCurrentPosition()
            self.status.character_name = character_name
        else:
            self.status.character_name = DEFAULT_CHARACTER_NAME

    def move(self, direction: Direction) -> None:
        self.status.current_position = self.character.moveDirection(direction)
        self.set_current_move_count(self.status.move_count)


    def set_character_position(self, xycoordinates: tuple) -> None:
        self.status.current_position = xycoordinates

    def set_current_move_count(self, move_count: int) -> None:
        self.status.move_count = move_count + 1

    def getTotalPositions(self) -> int:
        # TODO: IMPLEMENT THIS TO GET THE TOTAL POSITIONS FROM THE MAP - - exists to be
        # testable
        return GameMap.getTotalPositions(self)

    
