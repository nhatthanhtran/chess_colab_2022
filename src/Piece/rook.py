# -*- coding: utf-8 -*-
"""
Rook Class
"""

from piece import Piece
from helper import InBound


class Rook(Piece):
    def __init__(self, strColor, intCurXPos, intCurYPos):
        super().__init__(strColor, intCurXPos, intCurYPos, False)
        self.blnMoved = False

    def PossibleMoves(self):
        lstPosMoves = []
        # East (+=) direction move
        i = self.intCurXPos
        j = self.intCurYPos
        lstEMoves = []

        while InBound(i+1, j):
            lstEMoves.append([i+1, j])
            i += 1
        lstPosMoves.append(lstEMoves)

        # North (=+) direction move
        i = self.intCurXPos
        j = self.intCurYPos
        lstNMoves = []

        while InBound(i, j+1):
            lstNMoves.append([i, j+1])
            j += 1
        lstPosMoves.append(lstNMoves)

        # West (-=) direction move
        i = self.intCurXPos
        j = self.intCurYPos
        lstWMoves = []

        while InBound(i-1, j):
            lstWMoves.append([i-1, j])
            i -= 1
        lstPosMoves.append(lstWMoves)

        # South (=-) direction move
        i = self.intCurXPos
        j = self.intCurYPos
        lstEMoves = []

        while InBound(i, j-1):
            lstEMoves.append([i, j-1])
            j -= 1
        lstPosMoves.append(lstEMoves)

        return lstPosMoves

    def Capture(self):
        self.blnCapture = True

    def Move(self, intNewXPos, intNewYPos):
        if InBound(intNewXPos, intNewYPos):

            self.intCurXPos = intNewXPos
            self.intCurYPos = intNewYPos
            self.blnMoved = True
