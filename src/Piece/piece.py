# -*- coding: utf-8 -*-
"""
Abstract class piece that will be a base class for all the pieces in a chess 
board
"""
from abc import ABC, abstractmethod


class Piece(ABC):
    @abstractmethod
    def __init__(self, str_color, int_cur_x_pos, int_cur_y_pos, bln_captured):
        self.str_color = str_color
        self.int_cur_x_pos = int_cur_x_pos
        self.int_cur_y_pos = int_cur_y_pos
        self.bln_captured = bln_captured
