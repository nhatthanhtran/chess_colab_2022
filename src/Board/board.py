"""Board class
"""

from space import Space

INT_BOARDSIZE = 8 # Gloablal constant board side length in spaces

"""Assuming upper left corner is board[0][0] and white
"""

class Board:
    def __init__(self):
        _strColor + ("white" if (i + j) % 2 == 0 else "black")
        board = [[Space()]] # Need to create 2d array, DO NOT RUN BROKEN
        for i in range(INT_BOARDSIZE):
            for j in range(INT_BOARDSIZE):
                self.board[i][j] = Space(_strColor) # Set alternating space color
