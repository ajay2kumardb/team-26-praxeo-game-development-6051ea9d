from unittest import TestCase
from levelup.controller import GameController
from levelup.character import Character
from levelup.position import Position
class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None

    def test_move(self):
        testObj = GameController()
        character= Character("Joyce")
        testObj.create_character(character)
        testObj.move("s")
        self.assertEqual(character.getCurrentPosition(), (0, 1))

    def test_setcharacterposition(self):
        testObj = GameController()
        character= Character("Joyce")
        testObj.create_character(character)
        testObj.set_character_position((3,0))
        self.assertEqual(testObj.status.current_position, (3,0))

    def test_setCurrentMoveCount(self):
        testObj = GameController()
#      testObj.status.move_count = 1
        testObj.set_current_move_count(1)
        self.assertEqual(testObj.status.move_count, 1)
        

    def test_getTotalPositions(self):
        testObj = GameController()
        testObj.start_game()
        totalPositions = 100
        self.assertEqual(testObj.get_total_positions, totalPositions)
