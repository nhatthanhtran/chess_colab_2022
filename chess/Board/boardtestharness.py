# This file is to test board set up and functionality during initial development only.
# Author: John Palacios

from nis import match
from operator import truediv
from unittest import case
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
