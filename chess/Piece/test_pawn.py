"""Testing board object in this file. Author: John Palacios
"""

# from chess.Board.board import Board
from chess.Piece.pawn import Pawn
"""Testing Space colors
"""

# test = Board()
# print(test.get_spaceColor(0, 0))


def test_pawn():

    test2 = Pawn("black", 1, 1, 1)

    assert test2.possible_moves() == [[[1, 2], [1, 3]], [[0, 2], [2, 2]]]
