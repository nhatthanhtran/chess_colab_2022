"""Board class
"""

from chess.Board.space import Space

from chess.Piece.pawn import Pawn

_INT_BOARDSIZE = 8  # Gloablal constant board side length in spaces

"""Assuming upper left corner is board[0][0] and white
"""


class Board:
    _board = [
        [None for _ in range(_INT_BOARDSIZE)] for _ in range(_INT_BOARDSIZE)
    ]  # Will hold spaces

    def __init__(self):
        for i in range(_INT_BOARDSIZE):
            for j in range(_INT_BOARDSIZE):
                str_color_ = "white" if (i + j) % 2 == 0 else "black"
                self._board[i][j] = Space(str_color_)

    # returns space color string
    @classmethod
    def get_spaceColor(self, i, j):
        return self._board[i][j].str_color

    # returns true of piece at (s_x, s_y) can be moved to (d_x, d_y)
    @classmethod
    def validate_move(s_x, s_y, d_x, d_y):
        _piece = self_board[s_x][s_y].get_piece()  # Do not use, under construction
        _piece_type = type(_piece)

        # Testing type function
        return _piece_type
