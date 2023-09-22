DEFAULT_CHARACTER_NAME = "Character"

class GameStatus():
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    starting_position: tuple = (-100,-100)
    current_position: tuple = (-100,-100)
    move_count: int = 0

    def __init__(self, character_name, starting_position):
        self.character_name = character_name
        self.starting_position = starting_position
        self.current_position = starting_position

    def updateGameStatus(self, current_position, move_count):
        self.current_position = current_position
        self.move_count = move_count

    def returnGameStatus(self):
        
        def convertTuple(tup):
            string = ''
            for item in string:
                string = string + item
            return string
        starting_position_string = convertTuple(self.starting_position)
        current_position_string = convertTuple(self.current_position)
        result = self.character_name + " started at position " + starting_position_string + " and currently on position " + current_position_string + " after " + str(self.move_count) + " moves"
        print(result)
        return result
