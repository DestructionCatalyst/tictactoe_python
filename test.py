import unittest
from main import TicTacGame
import tic_tac_exceptions as tic_tac_ex


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()

    def test_creation(self):
        self.assertEqual('X', self.game.turn)
        for i in range(3):
            for j in range(3):
                self.assertIsNone(self.game.board[i][j])

    def test_input_validation(self):
        self.assertRaises(tic_tac_ex.CoordinatesTooShortError, self.lambda_validate('1-1'))
        self.assertRaises(tic_tac_ex.CoordinatesTooShortError, self.lambda_validate('2'))
        self.assertRaises(tic_tac_ex.CoordinatesTooLongError, self.lambda_validate('1 2 3'))
        self.assertRaises(tic_tac_ex.NonIntegerCoordinatesError, self.lambda_validate('2, 1'))
        self.assertRaises(tic_tac_ex.NonIntegerCoordinatesError, self.lambda_validate('2 q'))
        self.assertRaises(tic_tac_ex.CoordinatesTooSmallError, self.lambda_validate('1 0'))
        self.assertRaises(tic_tac_ex.CoordinatesTooBigError, self.lambda_validate('4 1'))
        self.assertRaises(tic_tac_ex.CoordinatesTooSmallError, self.lambda_validate('0 5'))
        self.game.make_turn(2, 2)
        self.assertRaises(tic_tac_ex.SpaceAlreadyOccupiedError, self.lambda_validate('2 2'))
        self.assertEqual((1, 1), self.game.validate_input('1 1'))
        self.assertEqual((3, 3), self.game.validate_input('  3    3 '))

    def lambda_validate(self, to_validate):
        return lambda: self.game.validate_input(to_validate)

    def test_make_turn(self):
        self.game.make_turn(1, 1)
        self.game.make_turn(1, 3)
        self.game.make_turn(2, 1)
        self.game.make_turn(2, 3)
        self.game.make_turn(3, 1)
        self.game.make_turn(3, 3)
        print(self.game.board)
        for i in range(3):
            self.assertEqual('X', self.game.board[0][i])
            self.assertEqual('0', self.game.board[2][i])
            self.assertEqual(None, self.game.board[1][i])

    def test_check_winner_x(self):
        self.game.make_turn(1, 1)
        self.game.make_turn(3, 1)
        self.game.make_turn(1, 3)
        self.game.make_turn(1, 2)
        self.game.make_turn(3, 3)
        self.game.make_turn(2, 2)
        self.game.make_turn(2, 3)
        self.assertEqual('X', self.game.check_winner())

    def test_check_winner_draw(self):
        self.game.make_turn(1, 1)
        self.game.make_turn(2, 2)
        self.game.make_turn(3, 3)
        self.game.make_turn(1, 2)
        self.game.make_turn(3, 2)
        self.game.make_turn(3, 1)
        self.game.make_turn(1, 3)
        self.game.make_turn(2, 3)
        self.game.make_turn(2, 1)
        print(self.game.board)
        self.assertEqual(None, self.game.check_winner())

    def test_check_winner_0(self):
        self.game.make_turn(2, 1)
        self.game.make_turn(2, 2)
        self.game.make_turn(3, 3)
        self.game.make_turn(1, 1)
        self.game.make_turn(2, 3)
        self.game.make_turn(1, 3)
        self.game.make_turn(3, 1)
        self.game.make_turn(1, 2)
        print(self.game.board)
        self.assertEqual('0', self.game.check_winner())


if __name__ == '__main__':
    unittest.main()
