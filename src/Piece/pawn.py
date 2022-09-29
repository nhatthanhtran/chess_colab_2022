# -*- coding: utf-8 -*-
"""
Pawn Class
"""
from piece import Piece
import numpy as np
from helper import blnInBound

class Pawn(Piece):
    def __init__(self, strColor, intCurXPos, intCurYPos, intMoveDir):
        super().__init__(strColor, intCurXPos, intCurYPos)
        self.blnMoved = False
        self.intMoveDir = intMoveDir

    def arrPossibleMoves(self):

        if (self.blnMoved):
            return(np.array([self.intCurXPos, self.intCurYPos+self.intMoveDir]))
        else:
            arrPosMoves = np.zeros((2, 2), dtype=np.intc)
            arrPosMoves[0, :] = np.array(
                [self.intCurXPos, self.intCurYPos+self.intMoveDir])
            arrPosMoves[1, :] = np.array(
                [self.intCurXPos, self.intCurYPos+self.intMoveDir*2])

            return(arrPosMoves)

    def Move(self, intNewXPos, intNewYPos):
        if blnInBound(intNewXPos, intNewYPos):

            self.intCurXPos = intNewXPos
            self.intCurYPos = intNewYPos
            self.blnMoved = True

