from unittest import TestCase
from levelup.map import GameMap

class TestMap(TestCase):
    def test_init(self):
        ARBITRARY_POSITIONS = 100
        testobj = GameMap(ARBITRARY_POSITIONS)
        self.assertEqual(ARBITRARY_POSITIONS, testobj.numPositions)

    def test_valid_pos(self):
        pos: tuple = (0,3)
        testobj = GameMap.isPositionValid(pos)
        self.assertEqual(testobj,True)

    def test_calc_pos(self):
        pos: tuple = (0,0)
        direction = "n"
        testobj = GameMap.calculatePosition(self, pos, direction)
        self.assertEqual(testobj,pos)
