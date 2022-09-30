# -*- coding: utf-8 -*-
"""
Queen Class
"""
from piece import Piece
from helper import InBound
from rook import Rook
from bishop import Bishop


class Queen(Piece):
    def __init__(self, strColor, intCurXPos, intCurYPos):
        super().__init__(strColor, intCurXPos, intCurYPos, False)

    def PossibleMoves(self):

        # Use the rook and bishop to get the moves
        lstRookMoves = Rook(self.strColor, self.intCurXPos,
                            self.intCurYPos).PossibleMoves()
        lstBishopMoves = Bishop(
            self.strColor, self.intCurXPos, self.intCurYPos).PossibleMoves()

        lstPosMoves = lstRookMoves + lstBishopMoves

        return lstPosMoves

    def Capture(self):
        self.Captured = True

    def Move(self, intNewXPos, intNewYPos):
        if InBound(intNewXPos, intNewYPos):
            self.intCurXPos = intNewXPos
            self.intCurYPos = intNewYPos
