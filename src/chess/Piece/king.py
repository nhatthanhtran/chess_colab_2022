# -*- coding: utf-8 -*-
"""
King Class
"""

from piece import Piece
from helper import InBound


class King(Piece):
    def __init__(self, strColor, intCurXPos, intCurYPos):
        super().__init__(strColor, intCurXPos, intCurYPos, False)
        self.blnMoved = False

    def PossibleMoves(self):
        lstPosMoves = []

        # Adding for each direction
        # East (+=)
        lstPosMoves = self.AddMove(
            lstPosMoves, self.intCurXPos+1, self.intCurYPos)
        # East North (++)
        lstPosMoves = self.AddMove(
            lstPosMoves, self.intCurXPos+1, self.intCurYPos+1)
        # North (=+)
        lstPosMoves = self.AddMove(
            lstPosMoves, self.intCurXPos, self.intCurYPos+1)
        # West North (-+)
        lstPosMoves = self.AddMove(
            lstPosMoves, self.intCurXPos-1, self.intCurYPos+1)
        # West (-=)
        lstPosMoves = self.AddMove(
            lstPosMoves, self.intCurXPos-1, self.intCurYPos)
        # West South (--)
        lstPosMoves = self.AddMove(
            lstPosMoves, self.intCurXPos-1, self.intCurYPos-1)
        # South (=-)
        lstPosMoves = self.AddMove(
            lstPosMoves, self.intCurXPos, self.intCurYPos-1)
        # East South (+-)
        lstPosMoves = self.AddMove(
            lstPosMoves, self.intCurXPos+1, self.intCurYPos-1)

        return lstPosMoves

    def AddMove(self, lstPosMove, intXPos, intYPos):
        if InBound(intXPos, intYPos):
            lstMove = []
            lstMove.append([intXPos, intYPos])
            lstPosMove.append(lstMove)

        return lstPosMove

    def Capture(self):
        self.blnCaptured = True

    def Move(self, intNewXPos, intNewYPos):
        if InBound(intNewXPos, intNewYPos):
            self.intCurXPos = intNewXPos
            self.intCurYPos = intNewYPos
            self.blnMoved = True
