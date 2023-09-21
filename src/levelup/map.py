from levelup.position import Position
class GameMap:
    numPositions = 100

    def __init__(self, numPositions):
        self.numPositions = 100

    def getTotalPositions():
        return numPositions 

    def getPositions():
        position = []

    def isPostionValid(positionCord):
        x, y = positionCord
        if (x < 0 or x > 9) or (y < 0 or  y > 9):
            return False
        else:
            return True