# This file is to test board set up and functionality during initial development only.
# Author: John Palacios


from chess.Board.board import Board
from chess.Piece.bishop import Bishop
from chess.Piece.king import King
from chess.Piece.knight import Knight
from chess.Piece.pawn import Pawn
from chess.Piece.queen import Queen
from chess.Piece.rook import Rook
from chess.Board.space import Space

# testing creation of a new board with pieces
test1 = Board()

print(test1.get_spaceColor(0, 0))
print(test1.get_board_state())
test1.move_piece(1, 6, 1, 4)
test1.move_piece(1, 4, 1, 3)
test1.move_piece(1, 3, 1, 2)
print(test1.get_board_state())
piece = test1.move_piece(0, 1, 1, 2)
print("captured: ", piece.bln_captured)
print(piece.int_cur_x_pos)
print(piece.int_cur_y_pos)
print(test1.get_board_state())