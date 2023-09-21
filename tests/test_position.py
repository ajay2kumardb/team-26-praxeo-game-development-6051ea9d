from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):

    def test_init(self):
        xCoordinates = 0
        yCoordinates = 0
        testObj = Position()
        self.assertEqual(xCoordinates, testObj.xCoordinates)
        self.assertEqual(yCoordinates, testObj.yCoordinates)

    def test_maxpos(self):
        xCoordinates_max = 9
        yCoordinates_max = 9  
        testObj = Position()
        self.assertEqual(xCoordinates_max, testObj.xCoordinates_max)
        self.assertEqual(yCoordinates_max, testObj.yCoordinates_max)      

    def test_minpos(self):
        xCoordinates_min = 0
        yCoordinates_min = 0  
        yCoordinates_min = 0  
        testObj = Position()
        self.assertEqual(xCoordinates_min, testObj.xCoordinates_min)
        self.assertEqual(yCoordinates_min, testObj.yCoordinates_min)  