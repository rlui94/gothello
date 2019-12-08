import unittest
from move import Move


class MyTestCase(unittest.TestCase):
    def test_constructor(self):
        mv = Move.from_desc("a3")
        self.assertEqual(mv.name(), "a3")
        mv = Move(1, 1)
        self.assertEqual(mv.name(), "b2")

    def test_digits_letters(self):
        mv = Move.from_desc("a3")
        self.assertEqual(mv.move_digit('1'), 0)
        self.assertEqual(mv.move_letter('c'), 2)


if __name__ == '__main__':
    unittest.main()
