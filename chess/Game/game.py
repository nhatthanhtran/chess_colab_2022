"""
Game Class
"""

from chess.Board.board import Board
from chess.Player.player import Player

class Game():
    def __init__(self):
        self.plr_white_player = Player("A", "white")
        self.plr_black_player = Player("B", "black")
        self.brd_board = Board()
        self.bln_end = False
    def play(self):
        pass

    
    







