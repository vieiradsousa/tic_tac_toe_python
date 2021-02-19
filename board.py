from __future__ import print_function


class Board(object):
    def __init__(self):
        self.positions = {'1': ' ', '2':  ' ', '3': ' ',
                          '4': ' ', '5':  ' ', '6': ' ',
                          '7': ' ', '8':  ' ', '9': ' '}

    def show(self):
        print(self.positions['1'] + '|' + self.positions['2'] + '|' + self.positions['3'])
        print('-+-+-')
        print(self.positions['4'] + '|' + self.positions['5'] + '|' + self.positions['6'])
        print('-+-+-')
        print(self.positions['7'] + '|' + self.positions['8'] + '|' + self.positions['9'])
