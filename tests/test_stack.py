import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):

    def test_starts_empty(self):
        s = Stack()
        self.assertEqual(s.contents, list())



if __name__ == "__main__":
    unittest.main()