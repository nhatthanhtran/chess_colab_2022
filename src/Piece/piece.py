# -*- coding: utf-8 -*-
"""
Abstract class piece that will be a base class for all the pieces in a chess 
board
"""
from abc import ABC, abstractmethod


class Piece(ABC):
    @abstractmethod
    def __init__(self, strColor, intCurXPos, intCurYPos, blnCaptured):
        self.strColor = strColor
        self.intCurXPos = intCurXPos
        self.intCurYPos = intCurYPos
        self.blnCaptured = blnCaptured
