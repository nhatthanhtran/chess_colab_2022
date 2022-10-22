"""Space class
"""

from chess.Piece.pawn import Pawn


class Space:
    def __init__(self, color):
        self.str_color = color
        self.bln_occupied = False
        self.pc_piece = None

    def occupy(self, piece):
        if self.bln_occupied:
            self.pc_piece.capture()
            self.pc_piece = piece
        else:
            self.bln_occupied = True
            self.pc_piece = piece

    def get_piece(self):
        if self.bln_occupied:
            return self.pc_piece
        else:
            return None
