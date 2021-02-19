from __future__ import print_function


class Player(object):
    def __init__(self, symbol):
        self.symbol = symbol

        print("Enter the player's name (" + symbol + ")!")
        self.name = raw_input("> ")

    def symbol(self):
        return self.symbol

    def name(self):
        return self.name
