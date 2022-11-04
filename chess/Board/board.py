"""Board class
"""

from ctypes import sizeof
from nis import match
from operator import truediv
from unittest import case
from chess.Piece.bishop import Bishop
from chess.Piece.king import King
from chess.Piece.knight import Knight
from chess.Piece.pawn import Pawn
from chess.Piece.piece import Piece
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
        self._lst_of_pieces = []
        # Set space color to checkered pattern
        for i in range(_INT_BOARDSIZE):
            for j in range(_INT_BOARDSIZE):
                str_color_ = "white" if (i + j) % 2 == 0 else "black"
                self._board[i][j] = Space(str_color_)

        # Populate board with new pieces
        self._create_pieces()
        self._set_pieces()

    # creates list of pieces to put on board at creation
    def _create_pieces(self):
        _piece_color = "white"

        # Hardcode backline order for now
        _lst_backline = [
            Rook,
            Knight,
            Bishop,
            King,
            Queen,
            Bishop,
            Knight,
            Rook,
        ]

        # Set up back white row
        for i in range(len(_lst_backline)):
            self._lst_of_pieces.append(_lst_backline[i](_piece_color, i, 0))

        # Set up white pawns
        for i in range(_INT_BOARDSIZE):
            self._lst_of_pieces.append(Pawn(_piece_color, i, 1, 1))

        _piece_color = "black"

        # Set up black back row
        for i in range(len(_lst_backline)):
            self._lst_of_pieces.append(_lst_backline[i](_piece_color, i, 7))

        # Set up black pawns
        for i in range(_INT_BOARDSIZE):
            self._lst_of_pieces.append(Pawn(_piece_color, i, 6, -1))

    # Set pieces where they belong (Only used durning initialization)
    def _set_pieces(self):
        for piece in self._lst_of_pieces:
            i = piece.int_cur_x_pos
            j = piece.int_cur_y_pos
            self._board[i][j].occupy(piece)

    # returns space color string
    def get_spaceColor(self, i, j):
        return self._board[i][j].str_color

    # returns true of piece at (s_x, s_y) can be moved to (d_x, d_y)
    def validate_move(self, s_x, s_y, d_x, d_y):
        piece = self._board[s_x][s_y].get_piece()
        valid_moves = []
        if piece:
            possible_moves = piece.possible_moves()  # by movement rules for piece
            piece_type = type(piece).__name__  # determine which piece

            # case pawn
            if piece_type == "Pawn":
                for i in range(len(possible_moves) - 1):
                    # check for blocking pieces
                    for j in range(len(possible_moves[i])):
                        x = possible_moves[i][j][0]
                        y = possible_moves[i][j][1]
                        if self._board[x][y].is_occupied():
                            continue
                        else:
                            valid_moves.append([x, y])

                # check attack spaces
                attack_Squares = possible_moves[-1]
                for i in range(len(attack_Squares)):
                    x = attack_Squares[i][0]
                    y = attack_Squares[i][1]
                    if self._board[x][y].str_color == piece.str_color:
                        continue
                    else:
                        valid_moves.append([x, y])
                print("pawn has valid moves", valid_moves)

            # Note: The king can move themselves into check. Will change later.
            elif piece_type in ["Bishop", "King", "Knight", "Rook", "Queen"]:
                for path in possible_moves:
                    for space in path:
                        x = space[0]
                        y = space[1]
                        # Blocked by piece of same color
                        if (
                            self._board[x][y].is_occupied()
                            and self._board[x][y].str_color == piece.str_color
                        ):
                            break
                        # End path by piece of opposite collor
                        elif self._board[x][y].is_occupied():
                            valid_moves.append([x, y])
                            break
                        # Space unoccupied
                        else:
                            valid_moves.append(space)
            else:
                print("validate_move case match error")
            return False
        # Now check if the given destination space is in the valid moves
        if [d_x, d_y] in valid_moves:
            return True
        else:
            return False

    # returns a list of lists representing the current state of board
    # format: [piece and color, [x_pos, y_pos]]
    def get_board_state(self):
        dct_pieces = {"Pawn":0, "Knight":1, "Bishop":2, "Rook":3, "Queen":4, "King":5}
        lst_piece_coord = []
        for p in self._lst_of_pieces:
            x = p.int_cur_x_pos
            y = p.int_cur_y_pos
            color = p.str_color
            p_type = type(p).__name__
            offset = 0 if color == "black" else 6
            lst_piece_coord.append([dct_pieces[p_type] + offset, [x, y]])
        
        return lst_piece_coord