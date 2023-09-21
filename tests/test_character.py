from unittest import TestCase
from levelup.character import Character
from levelup.position import Position
from levelup.map import GameMap

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_position(self):
        position = Position(3,2)
        testobj = Character("Ward")
        testobj.position = position
        self.assertEqual(testobj.position, position)


    def test_getName(self):
        name = "Michael"
        testobj = Character(name)
        self.assertEqual(testobj.getName(), name)

    def test_entermap(self):
            testobj = Character("Pam")
            map = GameMap(100)
            testobj.enterMap(map)

    def test_moveDirection(self):
        position: tuple = (3,4)
        direction = "n"
        map = GameMap(100)
        newPosition = map.calculatePosition(position, direction)
        self.assertFalse(newPoisition, position)
