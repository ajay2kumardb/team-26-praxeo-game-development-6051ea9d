from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):

     def test_init(self):
        ARBITRARY_COORDINATES = (8,0)

        testObj = Position(ARBITRARY_COORDINATES[0], ARBITRARY_COORDINATES[1])
        self.assertEqual(testObj.Coordinates, ARBITRARY_COORDINATES)   