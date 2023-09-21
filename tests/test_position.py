from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):

    def test_init(self):
        xCoordinates = 0
        yCoordinates = 0
        testObj = Position()
        self.assertEqual(xCoordinates, testObj.xCoordinates)
        self.assertEqual(yCoordinates, testObj.yCoordinates)
