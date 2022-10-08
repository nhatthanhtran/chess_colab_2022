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
        lst_pos_moves = self.add_move(
            lst_pos_moves, self.int_cur_x_pos+1, self.int_cur_y_pos)
        # East North (++)
        lst_pos_moves = self.add_move(
            lst_pos_moves, self.int_cur_x_pos+1, self.int_cur_y_pos+1)
        # North (=+)
        lst_pos_moves = self.add_move(
            lst_pos_moves, self.int_cur_x_pos, self.int_cur_y_pos+1)
        # West North (-+)
        lst_pos_moves = self.add_move(
            lst_pos_moves, self.int_cur_x_pos-1, self.int_cur_y_pos+1)
        # West (-=)
        lst_pos_moves = self.add_move(
            lst_pos_moves, self.int_cur_x_pos-1, self.int_cur_y_pos)
        # West South (--)
        lst_pos_moves = self.add_move(
            lst_pos_moves, self.int_cur_x_pos-1, self.int_cur_y_pos-1)
        # South (=-)
        lst_pos_moves = self.add_move(
            lst_pos_moves, self.int_cur_x_pos, self.int_cur_y_pos-1)
        # East South (+-)
        lst_pos_moves = self.add_move(
            lst_pos_moves, self.int_cur_x_pos+1, self.int_cur_y_pos-1)

        return lst_pos_moves

    def add_move(self, lst_pos_move, int_x_pos, int_y_pos):
        if in_bound(int_x_pos, int_y_pos):
            lst_move = []
            lst_move.append([int_x_pos, int_y_pos])
            lst_pos_move.append(lst_move)

        return lst_pos_move

    def capture(self):
        self.bln_captured = True

    def move(self, int_new_x_pos, int_new_y_pos):
        if in_bound(int_new_x_pos, int_new_y_pos):
            self.int_cur_x_pos = int_new_x_pos
            self.int_cur_y_pos = int_new_y_pos
            self.bln_moved = True


