"""Board class
"""

from nis import match
from operator import truediv
from unittest import case
from chess.Piece.bishop import Bishop
from chess.Piece.king import King
from chess.Piece.knight import Knight
from chess.Piece.pawn import Pawn
from chess.Piece.queen import Queen
from chess.Piece.rook import Rook
from chess.Board.space import Space


_INT_BOARDSIZE = 8  # Gloablal constant board side length in spaces

"""Assuming upper left corner is board[0][0] and white
"""


class Board:
    def __init__(self):
        self._board = [
            [None for _ in range(_INT_BOARDSIZE)] for _ in range(_INT_BOARDSIZE)
        ]
        self.lst_of_pieces = []
        for i in range(_INT_BOARDSIZE):
            for j in range(_INT_BOARDSIZE):
                str_color_ = "white" if (i + j) % 2 == 0 else "black"
                self._board[i][j] = Space(str_color_)

        # Populate board with new pieces
        self._create_pieces()
        self._set_pieces()

    # creates list of pieces to put on board at creation
    @classmethod
    def _create_pieces(self):
        _piece_color = "white"
        krook = Rook(_piece_color, 0, 0)
        self._lst_of_pieces.append(krook)
        kknight = Knight(_piece_color, 1, 0)
        self._lst_of_pieces.append(kknight)
        kbishop = Bishop(_piece_color, 2, 0)
        self._lst_of_pieces.append(kbishop)
        king = King(_piece_color, 3, 0)
        self._lst_of_pieces.append(king)
        queen = Queen(_piece_color, 4, 0)
        self._lst_of_pieces.append(queen)
        qbishop = Bishop(_piece_color, 5, 0)
        self._lst_of_pieces.append(qbishop)
        qknight = Knight(_piece_color, 6, 0)
        self._lst_of_pieces.append(qknight)
        qrook = Rook(_piece_color, 7, 0)
        self._lst_of_pieces.append(qrook)
        for i in range(_INT_BOARDSIZE):
            self._lst_of_pieces.append(Pawn(_piece_color, i, 0))

        _piece_color = "black"
        krook = Rook(_piece_color, 0, 7)
        self._lst_of_pieces.append(krook)
        kknight = Knight(_piece_color, 1, 7)
        self._lst_of_pieces.append(kknight)
        kbishop = Bishop(_piece_color, 2, 7)
        self._lst_of_pieces.append(kbishop)
        king = King(_piece_color, 3, 7)
        self._lst_of_pieces.append(king)
        queen = Queen(_piece_color, 4, 7)
        self._lst_of_pieces.append(queen)
        qbishop = Bishop(_piece_color, 5, 7)
        self._lst_of_pieces.append(qbishop)
        qknight = Knight(_piece_color, 6, 7)
        self._lst_of_pieces.append(qknight)
        qrook = Rook(_piece_color, 7, 7)
        self._lst_of_pieces.append(qrook)
        for i in range(_INT_BOARDSIZE):
            self._lst_of_pieces.append(Pawn(_piece_color, i, 7))

    # Set pieces where they belong (Only used durning initialization)
    @classmethod
    def _set_pieces(self):
        for piece in self._lst_of_pieces:
            i = piece.int_cur_x_pos
            j = piece.int_int_y_pos
            self._board[i][j].occupy(piece)

    # returns space color string
    @classmethod
    def get_spaceColor(self, i, j):
        return self._board[i][j].str_color

    # returns true of piece at (s_x, s_y) can be moved to (d_x, d_y)
    @classmethod
    def validate_move(self, s_x, s_y, d_x, d_y):
        _piece = self._board[s_x][s_y].get_piece()
        if _piece:
            _possible_moves = _piece.possible_moves()
            _piece_type = type(_piece).__name__

            if _piece_type == "Pawn":
                print("pawn has moves", _possible_moves)
            elif _piece_type == "Bishop":
                print("bishop has moves", _possible_moves)
            else:
                print("validate_move case match error")
            return True
        else:
            return False
