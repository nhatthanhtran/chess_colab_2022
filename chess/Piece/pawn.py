# -*- coding: utf-8 -*-
"""
Pawn Class
"""
from chess.Piece.piece import Piece
import numpy as np
from chess.Piece.helper import in_bound


class Pawn(Piece):
    def __init__(self, str_color, int_cur_x_pos, int_cur_y_pos, int_move_dir):
        super().__init__(str_color, int_cur_x_pos, int_cur_y_pos, False)
        self.bln_moved = False
        self.int_move_dir = int_move_dir

    def possible_moves(self):
        lst_pos_moves = []

        # Check if the pawn moved or not.
        if self.bln_moved:
            if in_bound(self.int_cur_x_pos, self.int_cur_y_pos + self.int_move_dir):
                lst_pos_moves.append(
                    [self.int_cur_x_pos, self.int_cur_y_pos + self.int_move_dir]
                )
            else:
                lst_pos_moves.append([])

        else:
            if in_bound(self.int_cur_x_pos, self.int_cur_y_pos + self.int_move_dir):
                lst_moves = []
                lst_moves.append(
                    [self.int_cur_x_pos, self.int_cur_y_pos + self.int_move_dir]
                )

                if in_bound(
                    self.int_cur_x_pos, self.int_cur_y_pos + self.int_move_dir * 2
                ):
                    lst_moves.append(
                        [self.int_cur_x_pos, self.int_cur_y_pos + self.int_move_dir * 2]
                    )

                lst_pos_moves.append(lst_moves)
            else:
                lst_pos_moves.append([])

        # get the attack moves
        lst_moves = []
        # -+
        if in_bound(self.int_cur_x_pos - 1, self.int_cur_y_pos + self.int_move_dir):
            lst_moves.append(
                [self.int_cur_x_pos - 1, self.int_cur_y_pos + self.int_move_dir]
            )
        if in_bound(self.int_cur_x_pos + 1, self.int_cur_y_pos + self.int_move_dir):
            lst_moves.append(
                [self.int_cur_x_pos + 1, self.int_cur_y_pos + self.int_move_dir]
            )

        if lst_moves:
            lst_pos_moves.append(lst_moves)

        return lst_pos_moves

    def move(self, int_new_x_pos, int_new_y_pos):
        if in_bound(int_new_x_pos, int_new_y_pos):

            self.int_cur_x_pos = int_new_x_pos
            self.int_cur_y_pos = int_new_y_pos
            self.bln_moved = True

    def capture(self):
        self.bln_captured = True
