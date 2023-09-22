from levelup.position import Position
class GameMap:
    numPositions = 100

    def __init__(self, numPositions):
        self.numPositions = 100

    def getTotalPositions(self):
        return numPositions 

    def getPositions(self):
        positions = []
        x = 0
        y = 0
        cords: tuple = (x,y)
        positions.append(cords)
        while y < 9:
            while x < 9:
                x = x + 1
                cords: tuple = (x,y)
                positions.append(cords)
            x = 0
            y = y + 1
            cords: tuple = (x,y)
            positions.append(cords)


    def isPositionValid(positionCord):
        x, y = positionCord
        if (x < 0 or x > 9) or (y < 0 or  y > 9):
            return False
        else:
            return True
    
    def calculatePosition(self, position, direction):
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
            case _:
                x = x
                y = y
        a = a + x
        b = b + y
        pos: tuple = (a,b)
        valid = GameMap.isPositionValid(pos)
        
        #up move count by 1
        if valid:
            return pos
        else:
            return position
        
        
