# -*- coding: utf-8 -*-
"""
Pawn Class
"""
from piece import Piece
import numpy as np


class Pawn(Piece):
    def __init__(self, strColor, intCurXPos, intCurYPos):
        super().__init__(strColor, intCurXPos, intCurYPos)
        self.blnMoved = False

    def arrPossibleMoves(self):
        if self.strColor == "BLACK":
            intMoveDir = -1
        else:
            intMoveDir = 1

        if (self.blnMoved):
            return(np.array([self.intCurXPos, self.intCurYPos+intMoveDir]))
        else:
            arrPosMoves = np.zeros((2, 2), dtype=np.intc)
            arrPosMoves[0, :] = np.array(
                [self.intCurXPos, self.intCurYPos+intMoveDir])
            arrPosMoves[1, :] = np.array(
                [self.intCurXPos, self.intCurYPos+intMoveDir*2])

            return(arrPosMoves)

    def Move(self, intNewXPos, intNewYPos):
        self.intCurXPos = intNewXPos
        self.intCurYPos = intNewYPos
        self.blnMoved = True
