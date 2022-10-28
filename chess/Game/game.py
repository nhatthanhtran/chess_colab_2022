"""
Game Class
"""

from chess.Board.board import Board
from chess.Player.player import Player

class Game():
    def __init__(self):
        plr_white = Player("A", "white")
        plr_black = Player("B", "black")
        self.lst_players = [plr_white, plr_black]
        self.brd_board = Board()
        self.bln_end = False
        self.bln_whos_turn = True # Base on RBG: False (0) is black True (1) is white
        self.int_turn_counter = 1
    def play(self):
        while not self.bln_end:

            # Get user input
            int_cur_x, int_cur_y, int_nxt_x, int_nxt_y = self._get_player_move()
            self._update_player(
                self.lst_players[self.bln_whos_turn],
                int_cur_x,
                int_cur_y,
                int_nxt_x,
                int_nxt_y,
            )

            # draw the current board
            self._draw_board()

            # check win condition
            if self.brd_board.locked():
                self._game_end()
                break
            
            # update turn
            self._update_turn()

            

    def _game_end(self):
        self.bln_end = True

    def game_save(self):
        pass

    def _update_turn(self):
        self.bln_whos_turn = not self.bln_whos_turn
        self.int_turn_counter += 1

    def _draw_board(self):
        self.brd_board.draw()

    def _update_player(self, plr_player: Player, int_cur_x, int_cur_y, int_nxt_x, int_nxt_y):
        
        plr_player.append_move(
            self.brd_board.get_piece(int_cur_x, int_cur_y),
            self.brd_board.get_space(int_nxt_x,int_nxt_y)
        )

        if self.brd_board.get_piece(int_nxt_x, int_nxt_y):
            plr_player.capture_piece(self.brd_board.get_piece(int_nxt_x, int_nxt_y))
    

    def _get_player_move(self):

        # Wait for user inputs from UI here

        if self.bln_whos_turn: # white
            return 0, 0, 1, 1
        else: # black
            return 7, 7, 7, 6

    







