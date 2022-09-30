# -*- coding: utf-8 -*-
"""
Knight Class
"""

from piece import Piece
from helper import *


class Knight(Piece):
    def __init__(self, strColor, intCurXPos, intCurYPos):
        super().__init__(strColor, intCurXPos, intCurYPos, False)

    def PossibleMoves(self):
        lstPosMoves = []

        # 2East1North (+2+1)
        lstMoves = []
        if InBound(self.intCurXPos+2, self.intCurYPos+1):
            lstMoves.append([self.intCurXPos+2, self.intCurYPos+1])
            lstPosMoves.append(lstMoves)

        # 2East1South (+2-1)
        lstMoves = []
        if InBound(self.intCurXPos+2, self.intCurYPos-1):
            lstMoves.append([self.intCurXPos+2, self.intCurYPos-1])
            lstPosMoves.append(lstMoves)

        # 1East2North (+1+2)
        lstMoves = []
        if InBound(self.intCurXPos+1, self.intCurYPos+2):
            lstMoves.append([self.intCurXPos+1, self.intCurYPos+2])
            lstPosMoves.append(lstMoves)

        # 1West2North (-1+2)
        lstMoves = []
        if InBound(self.intCurXPos-1, self.intCurYPos+2):
            lstMoves.append([self.intCurXPos-1, self.intCurYPos+2])
            lstPosMoves.append(lstMoves)

        # 2West1North (-2+1)
        lstMoves = []
        if InBound(self.intCurXPos-2, self.intCurYPos+1):
            lstMoves.append([self.intCurXPos-2, self.intCurYPos+1])
            lstPosMoves.append(lstMoves)

        # 2West1South (-2-1)
        lstMoves = []
        if InBound(self.intCurXPos-2, self.intCurYPos-1):
            lstMoves.append([self.intCurXPos-2, self.intCurYPos-1])
            lstPosMoves.append(lstMoves)

        # 1West2South (-1-2)
        lstMoves = []
        if InBound(self.intCurXPos-1, self.intCurYPos-2):
            lstMoves.append([self.intCurXPos-1, self.intCurYPos-2])
            lstPosMoves.append(lstMoves)

        # 1East2South (+1-2)
        lstMoves = []
        if InBound(self.intCurXPos+1, self.intCurYPos-2):
            lstMoves.append([self.intCurXPos+1, self.intCurYPos-2])
            lstPosMoves.append(lstMoves)

        return lstPosMoves

    def Capture(self):
        self.blnCaptured = True

    def Move(self, intNewXPos, intNewYPos):
        if InBound(intNewXPos, intNewYPos):
            self.intCurXPos = intNewXPos
            self.intCurYPos = intNewYPos
