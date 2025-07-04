import time
from player import Player, ComputerPlayer, HumanPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def make_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def board_nums():
        number_board = [[str(i*3 + j) for j in range(3)] for i in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square, letter):
        # check row for winner
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind +1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check columns
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.board_nums()

    letter = 'X' #starting letter

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to {square}')
                game.make_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                return letter

        letter = 'O' if letter == 'X' else 'X' # switch player after a move

        time.sleep(0.5)

    if print_game:
        print("It's a tie!")

if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
