import io
import unittest
from main import TicTacGame
import tic_tac_exceptions as tic_tac_ex
import sys


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()

    def test_creation(self):
        self.assertEqual('X', self.game.turn)
        for i in range(3):
            for j in range(3):
                self.assertIsNone(self.game.board[i][j])

    def test_input_validation(self):
        self.game.make_turn(2, 2)
        lst = [(tic_tac_ex.CoordinatesTooShortError, ['1-1', '2']),
               (tic_tac_ex.CoordinatesTooLongError, ['1 2 3']),
               (tic_tac_ex.NonIntegerCoordinatesError, ['2, 1', '2 q']),
               (tic_tac_ex.CoordinatesTooSmallError, ['1 0', '-2 1']),
               (tic_tac_ex.CoordinatesTooBigError, ['4 1', '2 100']),
               (tic_tac_ex.SpaceAlreadyOccupiedError, ['2 2'])]
        for exception, entries in lst:
            with self.assertRaises(exception):
                for entry in entries:
                    self.game.validate_input(entry)
        self.assertEqual((1, 1), self.game.validate_input('1 1'))
        self.assertEqual((3, 3), self.game.validate_input('  3    3 '))

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

    def test_game(self):
        actual_stdout = sys.stdout
        dummy_file = io.StringIO()
        sys.stdout = dummy_file
        turns_file = io.StringIO("1 1\n2 2\n1 2\n3 3\n1 3")
        self.game.start_game(turns_file.readline)
        dummy_file.seek(794)
        self.assertEqual("???????????????? ????????????????\n", dummy_file.read())
        sys.stdout.close()
        sys.stdout = actual_stdout


if __name__ == '__main__':
    unittest.main()
