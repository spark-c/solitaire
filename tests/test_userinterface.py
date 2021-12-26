import unittest
from src.board import Board
from src.userinterface import UserInterface, UserInput


class TestUserInput(unittest.TestCase):

    def setUp(self) -> None:
        b = Board()
        self.ui = UserInterface(b)
        self.input_string = " hello!@#$%^&*()-=\\/.,';: `~world123 "


    def test_clean_removes_special_chars(self):
        input_string = self.input_string
        user_input = UserInput(raw=input_string)

        self.assertEqual(user_input.clean, "hello-world123") #type:ignore

    
    def test_is_valid_accepts_help(self):
        input_string = "HeLp"
        user_input = UserInput(raw=input_string)

        self.assertTrue(user_input.is_valid)


    def test_is_valid_requires_three_chars(self):
        input_strings = ["01", "0123"]
        for string in input_strings:
            user_input = UserInput(raw=string)

            self.assertFalse(user_input.is_valid)


    def test_is_valid_prevents_duplicate_src_dest(self):
        input_string = "331"
        user_input = UserInput(raw=input_string)

        self.assertFalse(user_input.is_valid)

    
    def test_extra_command_flag(self):
        input_string = "help"
        user_input = UserInput(raw=input_string)
        user_input.is_valid

        self.assertTrue(user_input.extra_command)


    def test_ParsedCmd_normal_move(self):
        input_string = "012"
        user_input = UserInput(raw=input_string)
        user_input.is_valid
        
        self.assertEqual(
            user_input.parsed,
            {
                "command": "012",
                "src": "0",
                "dest": "1",
                "amt": 2
            }
        )


    def test_ParsedCmd_extra_command(self):
        input_string = "s"
        user_input = UserInput(raw=input_string)
        user_input.is_valid
        
        self.assertEqual(
            user_input.parsed,
            {
                "command": "s",
                "src": "",
                "dest": "",
                "amt": 0
            }
        )


class TestUserInterface(unittest.TestCase):

    def setUp(self) -> None:
        b = Board()
        self.ui = UserInterface(b)
        self.user_in = " hello!@#$%^&*()-=\\/.,';: `~world123 "


    def test_validate_accepts_help(self):
        # user_in = self.user_in
        # self.ui._get_input(manual_input=user_in)
        # self.ui._validate(self.ui.current_input)
        pass


if __name__ == "__main__":
    unittest.main()