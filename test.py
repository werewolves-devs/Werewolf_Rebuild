from management import game
import unittest

class Test_Board(unittest.TestCase):
    def test_example(self):

        self.assertEqual(True,True)

    def test_signup(self):
        with self.assertRaises(ValueError):
            game.signup("Yomomma")
        game.signup(248158876799729664,'😏')


if __name__ == '__main__':
    unittest.main()
