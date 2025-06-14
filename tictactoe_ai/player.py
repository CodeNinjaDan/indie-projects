import random
import math

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True

            except ValueError:
                print('Invalid square. Please try again.')

        return val


class ProComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # get square based off minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, snap, player):  # snap represents the game taking a snapshot of the board at every stage
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # check if previous move is a winner
        # base case
        if snap.current_winner == other_player:
            # return position and score 4 minimax to work
            return {'position': None,
                    'score': 1 * (snap.num_empty_squares() + 1) if other_player == max_player else -1 * (
                                snap.num_empty_squares() + 1)}

        elif not snap.empty_squares():
            return {'position': None, 'score': 0}

        # Initialize some dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # maximize each score
        else:
            best = {'position': None, 'score': math.inf}  # minimize each score

        for possible_move in snap.available_moves():
            # 1. make a move try that spot
            snap.make_move(possible_move, player)
            # 2. recurse using minimax to simulate a game after that move
            sim_score = self.minimax(snap, other_player)  # alternate players
            # 3. undo the move
            snap.board[possible_move] = ' '
            snap.current_winner = None
            sim_score['position'] = possible_move
            # 4. update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best