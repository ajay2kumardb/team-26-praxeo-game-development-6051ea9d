from levelup.position import Position
class GameMap:
    numPositions = 100

    def __init__(self, numPositions):
        self.numPositions = 100

    def getTotalPositions():
        return numPositions 

    def getPositions():
        position = []

    def isPositionValid(positionCord):
        x, y = positionCord
        if (x < 0 or x > 9) or (y < 0 or  y > 9):
            return False
        else:
            return True
    
    def calculatePosition(position,direction):
        x = 0
        y = 0
        a, b = position
        match direction:
            case "n":
                y = y - 1
            case "s":
                y = y + 1
            case "e":
                x = x + 1
            case "w":
                x = x - 1
        a = a + x
        b = b + y
        pos: tuple = (a,b)
        valid = GameMap.isPositionValid(pos)
        
        #up move count by 1
        if valid:
            return pos
        else:
            return position
        
        
