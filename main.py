from board import Board
from game import Game
from player import Player

import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    keep_playing = 'y'
    while keep_playing == 'y':
        # CLEARING THE SCREEN
        os.system('cls' if os.name == 'nt' else 'clear')

        # CREATING THE GAME
        game = Game(Board(), Player('X'), Player('O'))

        # START THE MOVES
        for i in range(9):
            game.board.show()
            game.turn()

            if not game.is_tied() and not game.is_won():
                game.next_player()
            else:
                print("Do want to play Again?(y/n)")
                keep_playing = raw_input("> ")
                break
    else:
        print("Thanks for playing!!!")
