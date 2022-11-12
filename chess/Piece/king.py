# -*- coding: utf-8 -*-
"""
King Class
"""

from chess.Piece.piece import Piece
from chess.Piece.helper import in_bound


class King(Piece):
    def __init__(self, str_color, int_cur_x_pos, int_cur_y_pos):
        super().__init__(str_color, int_cur_x_pos, int_cur_y_pos, False)
        self.bln_moved = False

    def possible_moves(self):
        lst_pos_moves = []

        # Adding for each direction
        # East (+=)
        lst_pos_moves = self._add_move(
            lst_pos_moves, self.int_cur_x_pos + 1, self.int_cur_y_pos
        )
        # East North (++)
        lst_pos_moves = self._add_move(
            lst_pos_moves, self.int_cur_x_pos + 1, self.int_cur_y_pos + 1
        )
        # North (=+)
        lst_pos_moves = self._add_move(
            lst_pos_moves, self.int_cur_x_pos, self.int_cur_y_pos + 1
        )
        # West North (-+)
        lst_pos_moves = self._add_move(
            lst_pos_moves, self.int_cur_x_pos - 1, self.int_cur_y_pos + 1
        )
        # West (-=)
        lst_pos_moves = self._add_move(
            lst_pos_moves, self.int_cur_x_pos - 1, self.int_cur_y_pos
        )
        # West South (--)
        lst_pos_moves = self._add_move(
            lst_pos_moves, self.int_cur_x_pos - 1, self.int_cur_y_pos - 1
        )
        # South (=-)
        lst_pos_moves = self._add_move(
            lst_pos_moves, self.int_cur_x_pos, self.int_cur_y_pos - 1
        )
        # East South (+-)
        lst_pos_moves = self._add_move(
            lst_pos_moves, self.int_cur_x_pos + 1, self.int_cur_y_pos - 1
        )
        if not lst_pos_moves:
            lst_pos_moves.append([])
        # return King castle moves
        # This will be a list of pair of move for the king
        # the first element will be the rook position
        # the second is the king position
        if not self.bln_moved:
            lst_pos_moves.append(self._get_castle_moves())

        else:
            lst_pos_moves.append([])

        return lst_pos_moves

    def _add_move(self, lst_pos_move, int_x_pos, int_y_pos):
        if in_bound(int_x_pos, int_y_pos):
            lst_move = []
            lst_move.append([int_x_pos, int_y_pos])
            lst_pos_move.append(lst_move)

        return lst_pos_move

    def _get_castle_moves(self):
        # E ++=
        lst_castle_moves = []
        if in_bound(self.int_cur_x_pos+2, self.int_cur_y_pos):
            lst_castle_moves.append([self.int_cur_x_pos+1, self.int_cur_y_pos])
            lst_castle_moves.append([self.int_cur_x_pos+2, self.int_cur_y_pos])
    
        # W --=
        if in_bound(self.int_cur_x_pos-2, self.int_cur_y_pos):
            lst_castle_moves.append([self.int_cur_x_pos-1, self.int_cur_y_pos])
            lst_castle_moves.append([self.int_cur_x_pos-2, self.int_cur_y_pos])

        return lst_castle_moves

    def capture(self):
        self.bln_captured = True

    def move(self, int_new_x_pos, int_new_y_pos):
        if in_bound(int_new_x_pos, int_new_y_pos):
            self.int_cur_x_pos = int_new_x_pos
            self.int_cur_y_pos = int_new_y_pos
            self.bln_moved = True
