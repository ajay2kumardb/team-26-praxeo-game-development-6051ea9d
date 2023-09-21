from levelup.map import GameMap

class Character:
 #   name = ""
    position = (0,0)
    map = GameMap

    def __init__(self, character_name):
        self.name = character_name
        print(self.name)

    def getName(self):
        return self.name
    
    def enterMap(self, map):
        self.map = GameMap(map)
