"""
A simple console tic-tac-toe game for 2 players in Python
"""

import tic_tac_exceptions as tic_tac_ex


class TicTacGame:
    """
    Main class of the game
    """
    def __init__(self):
        self.board = [[None] * 3, [None] * 3, [None] * 3]
        self.symbols_to_text = {'X': 'Крестики', '0': 'Нолики'}
        self.turn = 'X'

    def show_board(self):
        """
        Prints the game board to the console
        """
        self.draw_top()
        self.draw_line(0)
        self.draw_middle()
        self.draw_line(1)
        self.draw_middle()
        self.draw_line(2)
        self.draw_bottom()

    @staticmethod
    def draw_top():
        """
        Prints top line of the board
        """
        print('\u250c\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2510')

    def draw_line(self, line_number):
        """
        Print n-th line of the grid to the console
        :param line_number: number of line to print (0-2)
        """
        print('\u2502 ' + self.get_tile(0, line_number) +
              ' \u2502 ' + self.get_tile(1, line_number) +
              ' \u2502 ' + self.get_tile(2, line_number) +
              ' \u2502 ' + str(line_number + 1))

    def get_tile(self, x, y):
        """
        Get tile content to draw in the grid
        :param x: x coordinate of the tile (0-2)
        :param y: y coordinate of the tile (0-2)
        :return: whitespace if tile is empty, its content otherwise
        """
        tile = self.board[y][x]
        if tile is None:
            return ' '

        return tile

    @staticmethod
    def draw_middle():
        """
        Prints middle line of the board
        """
        print('\u251c\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2524')

    @staticmethod
    def draw_bottom():
        """
        Prints bottom line of the board
        """
        print('\u2514\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2518')
        print('  1   2   3  ')

    def validate_input(self, raw_input):
        """
        If input us correct, returns it as tuple(int, int), throws appropriate exception otherwise.
        Input string is considered correct if it consists of 2 integers from 1 to 3
        separated by whitespace(s).
        Leading ot trailing whitespaces do not affect the correctness.
        :param raw_input: input string to parse and validate
        :return: (x: int, y: int), 1 < x, y < 3 if input is correct
        """
        raw_coordinates = raw_input.strip().split()
        if len(raw_coordinates) < 2:
            raise tic_tac_ex.CoordinatesTooShortError()
        if len(raw_coordinates) > 2:
            raise tic_tac_ex.CoordinatesTooLongError()
        try:
            x, y = int(raw_coordinates[0].strip()), int(raw_coordinates[1].strip())
        except ValueError as ex:
            raise tic_tac_ex.NonIntegerCoordinatesError() from ex
        if x < 1 or y < 1:
            raise tic_tac_ex.CoordinatesTooSmallError()
        if x > 3 or y > 3:
            raise tic_tac_ex.CoordinatesTooBigError()
        if self.board[y - 1][x - 1] is not None:
            raise tic_tac_ex.SpaceAlreadyOccupiedError()
        return x, y

    def change_turn(self):
        """
        Changes active player from X to 0 or from 0 to X
        :return:
        """
        if self.turn == 'X':
            self.turn = '0'
        else:
            self.turn = 'X'

    def check_winner(self) -> object:
        """
        Checks the grid for 3 symbols in 1 row, column or diagonal,
        if it finds it, returns the symbol that's repeated 3 times
        :return: X or 0 if there is a winner, None otherwise
        """
        # check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2]:
                return self.board[i][0]
        # check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i]:
                return self.board[0][i]
        # check diagonals
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            return self.board[0][0]
        if self.board[2][0] == self.board[1][1] and self.board[2][0] == self.board[0][2]:
            return self.board[1][1]

        return None

    def start_game(self, input_function=lambda: input('Введите координаты через пробел: ')):
        """
        Controls the game process^ allows two players to repeatedly make turns,
         and shows the result of the game after it is ended
        :return:
        """
        winner = None
        turn_count = 0
        while winner is None and turn_count < 9:
            self.show_board()
            print('Ходят ' + self.symbols_to_text[self.turn])
            x, y = self.input_coordinates(input_function)
            self.make_turn(x, y)
            turn_count += 1
            winner = self.check_winner()

        self.show_board()
        if winner is None:
            print('Игра окончена! Ничья!')
        else:
            self.change_turn()
            print('Игра окончена! Победили ' + self.symbols_to_text[self.turn])

    def make_turn(self, x, y):
        """
        Place X or 0 in the tile (x, y) according to turn order
        :param x: x coordinate of the tile (0-2)
        :param y: y coordinate of the tile (0-2)
        """
        self.board[y - 1][x - 1] = self.turn
        self.change_turn()

    def input_coordinates(self, input_function):
        """
        Ask user to input coordinates until they insert them correctly
        In case of incorrect input, print an error message
        :return: (x: int, y: int)
        """
        coordinates = None
        while coordinates is None:
            raw_input = input_function()
            try:
                coordinates = self.validate_input(raw_input)
            except tic_tac_ex.CoordinatesTooShortError:
                print("Слишком мало координат или разделены не пробелом!")
            except tic_tac_ex.CoordinatesTooLongError:
                print("Слишком много координат!")
            except tic_tac_ex.NonIntegerCoordinatesError:
                print("Координаты не являются целыми числами или разделены не пробелом!")
            except tic_tac_ex.CoordinatesTooBigError:
                print("Одна из координат имеет слишком большое значение "
                      "(используйте от 1 до 3 включительно)")
            except tic_tac_ex.CoordinatesTooSmallError:
                print("Одна из координат имеет слишком маленькое значение "
                      "(используйте от 1 до 3 включительно)")
            except tic_tac_ex.SpaceAlreadyOccupiedError:
                print("Ход невозможен, так как выбранная клетка уже занята!")
        return coordinates


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
