# -*- coding: utf-8 -*-
"""
Rook Class
"""

from chess.Piece.piece import Piece
from chess.Piece.helper import in_bound


class Rook(Piece):
    def __init__(self, str_color, int_cur_x_pos, int_cur_y_pos):
        super().__init__(str_color, int_cur_x_pos, int_cur_y_pos, False)
        self.bln_moved = False

    def PossibleMoves(self):
        lst_pos_moves = []
        # East (+=) direction move
        i = self.int_cur_x_pos
        j = self.int_cur_y_pos
        lst_e_moves = []

        while in_bound(i + 1, j):
            lst_e_moves.append([i + 1, j])
            i += 1
        lst_pos_moves.append(lst_e_moves)

        # North (=+) direction move
        i = self.int_cur_x_pos
        j = self.int_cur_y_pos
        lst_n_moves = []

        while in_bound(i, j + 1):
            lst_n_moves.append([i, j + 1])
            j += 1
        lst_pos_moves.append(lst_n_moves)

        # West (-=) direction move
        i = self.int_cur_x_pos
        j = self.int_cur_y_pos
        lst_w_moves = []

        while in_bound(i - 1, j):
            lst_w_moves.append([i - 1, j])
            i -= 1
        lst_pos_moves.append(lst_w_moves)

        # South (=-) direction move
        i = self.int_cur_x_pos
        j = self.int_cur_y_pos
        lst_s_moves = []

        while in_bound(i, j - 1):
            lst_s_moves.append([i, j - 1])
            j -= 1
        lst_pos_moves.append(lst_s_moves)

        return lst_pos_moves

    def capture(self):
        self.bln_captured = True

    def move(self, int_new_x_pos, int_new_y_pos):
        if in_bound(int_new_x_pos, int_new_y_pos):

            self.int_cur_x_pos = int_new_x_pos
            self.int_cur_y_pos = int_new_y_pos
            self.bln_moved = True
