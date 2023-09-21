from unittest import TestCase
from levelup.map import GameMap

class TestMapInitWithPostition(TestCase):
    def test_init(self):
        ARBITRARY_POSITIONS = 100
        testobj = GameMap(ARBITRARY_POSITIONS)
        self.assertEqual(ARBITRARY_POSITIONS, testobj.numPositions)