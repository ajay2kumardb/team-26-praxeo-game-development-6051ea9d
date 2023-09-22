from levelup.map import GameMap
from levelup.position import Position
class Character:
 #   name = ""
    position: tuple = (0, 0)
    map = GameMap(100)

    def __init__(self, character_name):
        self.name = character_name
        print(self.name, self.map)

    def getName(self):
        return self.name
    
    def enterMap(self, Map):
        return GameMap(map)

    def moveDirection(self, direction):
        self.position = self.map.calculatePosition(self.position, direction)
        return self.position

    def getStartingPosition(self):
        return self.position