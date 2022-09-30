# -*- coding: utf-8 -*-
"""
Pawn Class
"""
from piece import Piece
import numpy as np
from helper import InBound


class Pawn(Piece):
    def __init__(self, strColor, intCurXPos, intCurYPos, intMoveDir):
        super().__init__(strColor, intCurXPos, intCurYPos, False)
        self.blnMoved = False
        self.intMoveDir = intMoveDir

    def PossibleMoves(self):
        lstPosMoves = []

        # Check if the pawn moved or not.
        if (self.blnMoved):
            if InBound(self.intCurXPos, self.intCurYPos+self.intMoveDir):
                lstPosMoves.append(
                    [self.intCurXPos, self.intCurYPos+self.intMoveDir])
            else:
                lstPosMoves.append([])

        else:
            if InBound(self.intCurXPos, self.intCurYPos+self.intMoveDir):
                lstMoves = []
                lstMoves.append(
                    [self.intCurXPos, self.intCurYPos+self.intMoveDir])

                if InBound(self.intCurXPos, self.intCurYPos+self.intMoveDir*2):
                    lstMoves.append(
                        [self.intCurXPos, self.intCurYPos+self.intMoveDir*2])

                lstPosMoves.append(lstMoves)
            else:
                lstPosMoves.append([])

        return lstPosMoves

    def Move(self, intNewXPos, intNewYPos):
        if InBound(intNewXPos, intNewYPos):

            self.intCurXPos = intNewXPos
            self.intCurYPos = intNewYPos
            self.blnMoved = True

    def Capture(self):
        self.Captured = True
