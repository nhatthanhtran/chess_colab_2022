"""
Player Class
"""


class Player:
    def __init__(self, str_name, str_player_color) -> None:
        self.str_name = str_name
        self.str_player_color = str_player_color
        self.lst_captured_pieces = []
        self.lst_moves = []

    def append_move(self, pc_player_piece, spc_move_to_space):
        # input: current player piece, space where the piece move next
        lst_move = []
        lst_move.append(type(pc_player_piece).__name__)
        lst_move.append(pc_player_piece.int_cur_x_pos)
        lst_move.append(pc_player_piece.int_cur_y_pos)

        if spc_move_to_space.get_piece():
            lst_move.append(type(spc_move_to_space.get_piece()).__name__)
        else:
            lst_move.append("None")

        self.lst_moves.append(lst_move)

    def append_captured_pieces(self, pc_capture_piece):
        self.lst_captured_pieces.append(pc_capture_piece)
