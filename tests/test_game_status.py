from unittest import TestCase
from levelup.status import GameStatus

class TestGameStatus(TestCase):

    def test_init(self):
        expected_running = False
        expected_character_name = "Character"    
        expected_starting_position = (0,0)   
        expected_current_position = (0,0)
        expected_move_count = 0
        testObj = GameStatus(expected_character_name, expected_starting_position)
        self.assertEqual(expected_running, testObj.running) 
        self.assertEqual(expected_character_name, testObj.character_name) 
        self.assertEqual(expected_starting_position,  testObj.current_position)
        self.assertEqual(expected_current_position,  testObj.current_position)
        self.assertEqual(expected_move_count, testObj.move_count)

    def test_update_status(self):
        expected_character_name = "John"   
        expected_starting_position = (0,0) 
        testObj = GameStatus(expected_character_name, expected_starting_position)  
        # Testing updated status
        expected_current_position = (2,3)
        expected_move_count = 1
        testObj.updateGameStatus(expected_current_position, expected_move_count)
        self.assertEqual(expected_current_position,  testObj.current_position)
        self.assertEqual(expected_move_count, testObj.move_count)
        self.assertEqual(expected_starting_position,  testObj.starting_position)

    def test_return_game_status(self):
        expected_character_name = "Betty"   
        expected_starting_position = (0,0) 
        testObj = GameStatus(expected_character_name, expected_starting_position)  
        # Updated status
        expected_current_position = (4,5)
        expected_move_count = 1
        testObj.updateGameStatus(expected_current_position, expected_move_count)
        # Testing string output
        expected_str = testObj.returnGameStatus()
        print(expected_str)
        self.assertIsInstance(expected_str, str)
