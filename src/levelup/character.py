from levelup.map import GameMap

class Character:
 #   name = ""
    position: tuple = (3, 4)
    map = GameMap(100)

    def __init__(self, character_name):
        self.name = character_name
        self.position: tuple = (3, 4)
        print(self.name)

    def getName(self):
        return self.name
    
    def enterMap(self, map):
        self.map = GameMap(map)

    def moveDirection(self, direction):
        self.position = self.map.calculatePosition(self.position, direction)
        return self.position