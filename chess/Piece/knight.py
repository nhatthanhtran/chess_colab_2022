# -*- coding: utf-8 -*-
"""
Knight Class
"""

from piece import Piece
from helper import *


class Knight(Piece):
    def __init__(self, str_color, int_cur_x_pos, int_cur_y_pos):
        super().__init__(str_color, int_cur_x_pos, int_cur_y_pos, False)

    def possible_moves(self):
        lst_pos_moves = []

        # 2East1North (+2+1)
        lst_moves = []
        if in_bound(self.int_cur_x_pos+2, self.int_cur_y_pos+1):
            lst_moves.append([self.int_cur_x_pos+2, self.int_cur_y_pos+1])
            lst_pos_moves.append(lst_moves)

        # 2East1South (+2-1)
        lst_moves = []
        if in_bound(self.int_cur_x_pos+2, self.int_cur_y_pos-1):
            lst_moves.append([self.int_cur_x_pos+2, self.int_cur_y_pos-1])
            lst_pos_moves.append(lst_moves)

        # 1East2North (+1+2)
        lst_moves = []
        if in_bound(self.int_cur_x_pos+1, self.int_cur_y_pos+2):
            lst_moves.append([self.int_cur_x_pos+1, self.int_cur_y_pos+2])
            lst_pos_moves.append(lst_moves)

        # 1West2North (-1+2)
        lst_moves = []
        if in_bound(self.int_cur_x_pos-1, self.int_cur_y_pos+2):
            lst_moves.append([self.int_cur_x_pos-1, self.int_cur_y_pos+2])
            lst_pos_moves.append(lst_moves)

        # 2West1North (-2+1)
        lst_moves = []
        if in_bound(self.int_cur_x_pos-2, self.int_cur_y_pos+1):
            lst_moves.append([self.int_cur_x_pos-2, self.int_cur_y_pos+1])
            lst_pos_moves.append(lst_moves)

        # 2West1South (-2-1)
        lst_moves = []
        if in_bound(self.int_cur_x_pos-2, self.int_cur_y_pos-1):
            lst_moves.append([self.int_cur_x_pos-2, self.int_cur_y_pos-1])
            lst_pos_moves.append(lst_moves)

        # 1West2South (-1-2)
        lst_moves = []
        if in_bound(self.int_cur_x_pos-1, self.int_cur_y_pos-2):
            lst_moves.append([self.int_cur_x_pos-1, self.int_cur_y_pos-2])
            lst_pos_moves.append(lst_moves)

        # 1East2South (+1-2)
        lst_moves = []
        if in_bound(self.int_cur_x_pos+1, self.int_cur_y_pos-2):
            lst_moves.append([self.int_cur_x_pos+1, self.int_cur_y_pos-2])
            lst_pos_moves.append(lst_moves)

        return lst_pos_moves

    def capture(self):
        self.bln_captured = True

    def move(self, int_new_x_pos, int_new_y_pos):
        if in_bound(int_new_x_pos, int_new_y_pos):
            self.int_cur_x_pos = int_new_x_pos
            self.int_cur_y_pos = int_new_y_pos
