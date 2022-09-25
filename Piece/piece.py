# -*- coding: utf-8 -*-
"""
Abstract class piece that will be a base class for all the pieces in a chess 
board
"""
from abc import ABC, abstractmethod


class Piece(ABC):

    strColor = ""
    intXCurrentPosition = 0
    intYCurrentPosition = 0

    @abstractmethod
    def setColor(self, strColor):
        pass

    @abstractmethod
    def setCurrentPosition(self, intXCurrentPosition, intYCurrentPosition):
        pass
