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
            int_white_cur_x, int_white_cur_y = 0, 0
            int_white_nxt_x, int_white_nxt_y = 1, 1
            self._update_player(
                self.plr_white,
                int_white_cur_x,
                int_white_cur_y,
                int_white_nxt_x,
                int_white_nxt_y,
            )

            # check win condition
            if self.brd_board.locked():
                self._game_end()
                break



            
            
            # black move
            int_black_cur_x, int_black_cur_y = 0, 0
            int_black_nxt_x, int_black_nxt_y = 1, 1
            self._update_player(
                self.plr_black,
                int_black_cur_x,
                int_black_cur_y,
                int_black_nxt_x,
                int_black_nxt_y,
            )
            # check win condition
            if self.brd_board.locked():
                self._game_end()

    def _game_end(self):
        self.bln_end = True

    def game_save(self):
        pass

    def _update_player(self, plr_player: Player, int_cur_x, int_cur_y, int_nxt_x, int_nxt_y):
        
        plr_player.append_move(
            self.brd_board.get_piece(int_cur_x, int_cur_y),
            self.brd_board.get_space(int_nxt_x,int_nxt_y)
        )

        if self.brd_board.get_piece(int_nxt_x, int_nxt_y):
            plr_player.capture_piece(self.brd_board.get_piece(int_nxt_x, int_nxt_y))
        


    







