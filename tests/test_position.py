from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):

     def test_init(self):
        xCoordinates = 5
        yCoordinates = 4
        testObj = Position(xCoordinates, yCoordinates)
        self.assertIsNotNone(testObj.xCoordinates)
        self.assertIsNotNone(testObj.yCoordinates)
        