"""Space class
"""

# from pathlib import Path
# from os import chdir
# init_path = Path(__file__)
# chdir('..')
# chdir('Piece')
# print(Path.cwd())
from chess.Piece.pawn import Pawn


class Space:
    def __init__(self, color):
        self.str_color = color
        self.bln_occupied = False

    @classmethod
    def occupy(piece):
        if self.bln_occupied:
            self.pc_piece.capture()
            self.pc_piece = piece
        else:
            self.pc_piece = piece

    @classmethod
    def get_piece(self):
        if self.bln_occupied:
            return self.pc_piece
        else:
            return None
