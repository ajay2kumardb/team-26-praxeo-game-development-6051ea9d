from unittest import TestCase
from levelup.character import Character
from levelup.position import Position

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_position(self):
        position = Position()
        testobj = Character("Ward")
        testobj.position = position
        self.assertEqual(testobj.position, position)


    def test_getName(self):
        name = "Michael"
        testobj = Character(name)
        self.assertEqual(testobj.getName(), name)

