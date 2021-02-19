from __future__ import print_function


class Game(object):
    def __init__(self, board, player_x, player_o):
        self.board = board
        self.player_x = player_x
        self.player_o = player_o
        self.player_to_play = self.player_x
        self.count = 0

    def turn(self):
        print("It's your turn, " + self.player_to_play.name + ". Move to which place?")
        move = raw_input("> ")

        while self.assign_to_board(move):
            print("That place is already filled. Move to which place?")

        self.count += 1

    def next_player(self):
        if self.player_to_play == self.player_x:
            self.player_to_play = self.player_o
        else:
            self.player_to_play = self.player_x

    def assign_to_board(self, move):
        print(self.board.positions[move])
        if self.board.positions[move] == ' ':
            self.board.positions[move] = self.player_to_play.symbol
            return True
        else:
            return False

    def is_won(self):
        result = False
        if self.count >= 5:
            # across the top
            if self.board.positions['1'] == self.board.positions['2'] == self.board.positions['3'] != ' ':
                result = True
            # across the middle
            elif self.board.positions['4'] == self.board.positions['5'] == self.board.positions['6'] != ' ':
                result = True
            # across the bottom
            elif self.board.positions['7'] == self.board.positions['8'] == self.board.positions['9'] != ' ':
                result = True
            # down the left side
            elif self.board.positions['1'] == self.board.positions['4'] == self.board.positions['7'] != ' ':
                result = True
            # down the middle
            elif self.board.positions['2'] == self.board.positions['5'] == self.board.positions['8'] != ' ':
                result = True
            # down the right side
            elif self.board.positions['3'] == self.board.positions['6'] == self.board.positions['9'] != ' ':
                result = True
            # diagonal
            elif self.board.positions['3'] == self.board.positions['5'] == self.board.positions['7'] != ' ':
                result = True
            # diagonal
            elif self.board.positions['1'] == self.board.positions['5'] == self.board.positions['9'] != ' ':
                result = True

        if result:
            self.board.show()
            print("\nGame Over.\n")
            print(" **** " + self.player_to_play.name + " won. ****")

        return result

    def is_tied(self):
        if self.count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            return True

        return False
