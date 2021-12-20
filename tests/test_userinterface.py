import unittest
from src.board import Board
from src.userinterface import UserInterface


class TestUserInterface(unittest.TestCase):

    def setUp(self) -> None:
        b = Board()
        self.ui = UserInterface(b)
        self.user_in = " hello!@#$%^&*()-=\\/.,';: `~world123 "


    def test_get_input_removes_special_chars(self):
        user_in = self.user_in
        self.ui._get_input(manual_input=user_in)

        self.assertEqual(self.ui.current_input.cleaned, "helloworld123") #type:ignore


    def test_get_input_preserves_original_input(self):
        user_in = self.user_in
        self.ui._get_input(manual_input=user_in)

        self.assertEqual(self.ui.current_input.raw, user_in) #type:ignore


    def test_validate_accepts_help(self):
        # user_in = self.user_in
        # self.ui._get_input(manual_input=user_in)
        # self.ui._validate(self.ui.current_input)
        pass


if __name__ == "__main__":
    unittest.main()