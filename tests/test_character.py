from unittest import TestCase
from levelup.character import Character
from levelup.position import Position

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_position(self):
        position = Position(10,1)
        character.position = position
        self.assertEqual(character.position, position)
