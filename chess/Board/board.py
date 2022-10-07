"""Board class
"""

from space import Space

INT_BOARDSIZE = 8 # Gloablal constant board side length in spaces

"""Assuming upper left corner is board[0][0] and white
"""

class Board:
    _board = [[None for _ in range(INT_BOARDSIZE)] for _ in range(INT_BOARDSIZE)] # Will hold spaces
    def __init__(self):
        for i in range(INT_BOARDSIZE):
            for j in range(INT_BOARDSIZE):
                str_color_ = "white" if (i + j) % 2 == 0 else "black"
                self._board[i][j] = Space(str_color_)

    @classmethod
    def get_spaceColor(self, i, j):
        return self._board[i][j].str_color
