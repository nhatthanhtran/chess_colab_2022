# -*- coding: utf-8 -*-
"""
Bishop Class
"""
from piece import Piece
from helper import InBound


class Bishop(Piece):
    def __init__(self, strColor, intCurXPos, intCurYPos):
        super().__init__(strColor, intCurXPos, intCurYPos, False)

    def PossibleMoves(self):
        lstPosMoves = []

        # East North (++) direction moves
        i = self.intCurXPos
        j = self.intCurYPos
        lstENMoves = []

        while InBound(i+1, j+1):
            lstENMoves.append([i+1, j+1])
            i += 1
            j += 1
        lstPosMoves.append(lstENMoves)

        # West North (-+) direction moves
        i = self.intCurXPos
        j = self.intCurYPos
        lstWNMoves = []

        while InBound(i-1, j+1):
            lstWNMoves.append([i-1, j+1])
            i -= 1
            j += 1
        lstPosMoves.append(lstWNMoves)

        # West South (--) direction moves
        i = self.intCurXPos
        j = self.intCurYPos
        lstWSMoves = []

        while InBound(i-1, j-1):
            lstWSMoves.append([i-1, j-1])
            i -= 1
            j -= 1
        lstPosMoves.append(lstWSMoves)

        # East South (+-) direction moves
        i = self.intCurXPos
        j = self.intCurYPos
        lstESMoves = []

        while InBound(i+1, j-1):
            lstESMoves.append([i+1, j-1])
            i += 1
            j -= 1

        lstPosMoves.append(lstESMoves)

        return lstPosMoves

    def Capture(self):
        self.blnCaptured = True

    def Move(self, intNewXPos, intNewYPos):
        if InBound(intNewXPos, intNewYPos):
            self.intCurXPos = intNewXPos
            self.intCurYPos = intNewYPos
