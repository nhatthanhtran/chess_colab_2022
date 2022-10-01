# -*- coding: utf-8 -*-
"""
Queen Class
"""
from piece import Piece
from helper import InBound
from rook import Rook
from bishop import Bishop


class Queen(Piece):
    def __init__(self, str_color, int_cur_x_pos, int_cur_y_pos):
        super().__init__(str_color, int_cur_x_pos, int_cur_y_pos, False)

    def possible_moves(self):

        # Use the rook and bishop to get the moves
        lst_rook_moves = Rook(self.str_color, self.int_cur_x_pos,
                            self.int_cur_y_pos).possible_moves()
        lst_bishop_moves = Bishop(
            self.str_color, self.int_cur_x_pos, self.int_cur_y_pos).possible_moves()

        return lst_rook_moves + lst_bishop_moves

    def capture(self):
        self.bln_captured = True

    def move(self, int_new_x_pos, int_new_y_pos):
        if in_bound(int_new_x_pos, int_new_y_pos):
            self.int_cur_x_pos = int_new_x_pos
            self.int_cur_y_pos = int_new_y_pos
