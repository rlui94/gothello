import unittest
import move


class MyTestCase(unittest.TestCase):
    def test_digit(self):
        mv = move.Move.from_coords(1, 2)
        self.assertEqual(mv.move_digit(self, '1'), 0)
        self.assertEqual(mv.move_letter(self, 'c'), 2)


if __name__ == '__main__':
    unittest.main()
