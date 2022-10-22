"""
Game Class
"""

from chess.Board.board import Board
from chess.Player.player import Player

class Game():
    def __init__(self):
        self.plr_white = Player("A", "white")
        self.plr_black = Player("B", "black")
        self.brd_board = Board()
        self.bln_end = False
    def play(self):
        while not self.bln_end:
            # white move
            pass
            
            
            # black move

    def game_end(self):
        pass

    def game_save(self):
        pass

    







