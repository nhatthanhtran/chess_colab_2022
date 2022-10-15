# -*- coding: utf-8 -*-
"""
Bishop Class
"""
from chess.Piece.piece import Piece
from chess.Piece.helper import in_bound


class Bishop(Piece):
    def __init__(self, str_color, int_cur_x_pos, int_cur_y_pos):
        super().__init__(str_color, int_cur_x_pos, int_cur_y_pos, False)

    def possible_moves(self):
        lst_pos_moves = []

        # East North (++) direction moves
        i = self.int_cur_x_pos
        j = self.int_cur_y_pos
        lst_en_moves = []

        while in_bound(i + 1, j + 1):
            lst_en_moves.append([i + 1, j + 1])
            i += 1
            j += 1
        lst_pos_moves.append(lst_en_moves)

        # West North (-+) direction moves
        i = self.int_cur_x_pos
        j = self.int_cur_y_pos
        lst_wn_moves = []

        while in_bound(i - 1, j + 1):
            lst_wn_moves.append([i - 1, j + 1])
            i -= 1
            j += 1
        lst_pos_moves.append(lst_wn_moves)

        # West South (--) direction moves
        i = self.int_cur_x_pos
        j = self.int_cur_y_pos
        lst_ws_moves = []

        while in_bound(i - 1, j - 1):
            lst_ws_moves.append([i - 1, j - 1])
            i -= 1
            j -= 1
        lst_pos_moves.append(lst_ws_moves)

        # East South (+-) direction moves
        i = self.int_cur_x_pos
        j = self.int_cur_y_pos
        lst_es_moves = []

        while in_bound(i + 1, j - 1):
            lst_es_moves.append([i + 1, j - 1])
            i += 1
            j -= 1

        lst_pos_moves.append(lst_es_moves)

        return lst_pos_moves

    def capture(self):
        self.bln_captured = True

    def move(self, int_new_x_pos, int_new_y_pos):
        if in_bound(int_new_x_pos, int_new_y_pos):
            self.int_cur_x_pos = int_new_x_pos
            self.int_cur_y_pos = int_new_y_pos
