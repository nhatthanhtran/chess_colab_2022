"""Testing board object in this file. Author: John Palacios
"""

# from chess.Board.board import Board
from chess.Piece.pawn import Pawn
"""Testing Space colors
"""

# test = Board()
# print(test.get_spaceColor(0, 0))

test2 = Pawn("black", 1, 1, 1)

print(test2.possible_moves())
