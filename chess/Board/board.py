"""Board class
"""

from unittest import case
from chess.Piece.bishop import Bishop
from chess.Piece.king import King
from chess.Piece.knight import Knight
from chess.Piece.pawn import Pawn
from chess.Piece.piece import Piece
from chess.Piece.queen import Queen
from chess.Piece.rook import Rook
from chess.Board.space import Space


_INT_BOARDSIZE = 8  # Gloablal constant board side length in spaces

"""Assuming upper left corner is board[0][0] and white
"""


class Board:
    def __init__(self):
        self._board = [
            [None for _ in range(_INT_BOARDSIZE)] for _ in range(_INT_BOARDSIZE)
        ]
        self._lst_of_pieces = []
        # Set space color to checkered pattern
        for i in range(_INT_BOARDSIZE):
            for j in range(_INT_BOARDSIZE):
                str_color_ = "white" if (i + j) % 2 == 0 else "black"
                self._board[i][j] = Space(str_color_)

        # Populate board with new pieces
        self._create_pieces()
        self._set_pieces()

    # creates list of pieces to put on board at creation
    def _create_pieces(self):
        _piece_color = "white"

        # Hardcode backline order for now
        _lst_backline = [
            Rook,
            Knight,
            Bishop,
            King,
            Queen,
            Bishop,
            Knight,
            Rook,
        ]

        # Set up back white row
        for i in range(len(_lst_backline)):
            self._lst_of_pieces.append(_lst_backline[i](_piece_color, i, 0))

        # Set up white pawns
        for i in range(_INT_BOARDSIZE):
            self._lst_of_pieces.append(Pawn(_piece_color, i, 1, 1))

        _piece_color = "black"

        # Set up black back row
        for i in range(len(_lst_backline)):
            self._lst_of_pieces.append(_lst_backline[i](_piece_color, i, 7))

        # Set up black pawns
        for i in range(_INT_BOARDSIZE):
            self._lst_of_pieces.append(Pawn(_piece_color, i, 6, -1))

    # Set pieces where they belong (Only used durning initialization)
    def _set_pieces(self):
        for piece in self._lst_of_pieces:
            i = piece.int_cur_x_pos
            j = piece.int_cur_y_pos
            self._board[i][j].occupy(piece)

    # returns space color string
    def get_space_color(self, i, j):
        return self._board[i][j].str_color

    # returns opposing color of given piece.
    def get_opposingColor(self, piece):
        color = piece.str_color
        if color == "white":
            return "black"
        else:
            return "white"

    # returns true of piece at (s_x, s_y) can be moved to (d_x, d_y)
    def validate_move(self, s_x, s_y, d_x, d_y):
        lst_valid_moves = self.get_valid_moves(s_x, s_y, d_x, d_y)
        return lst_valid_moves[0]

    # returns a list of lists representing the current state of board
    # format: [piece and color, [x_pos, y_pos]]
    # piece color: "Pawn":0, "Knight":1, "Bishop":2, "Rook":3, "Queen":4, "King":5 if
    # white add 6.
    def get_board_state(self):
        dct_pieces = {"Pawn": 0, "Knight": 1,
                      "Bishop": 2, "Rook": 3, "Queen": 4, "King": 5}
        lst_piece_coord = []
        for p in self._lst_of_pieces:
            if not p.bln_captured:
                x = p.int_cur_x_pos
                y = p.int_cur_y_pos
                color = p.str_color
                p_type = type(p).__name__
                offset = 0 if color == "black" else 6
                lst_piece_coord.append([dct_pieces[p_type] + offset, [x, y]])

        return lst_piece_coord

    # pc_attacker captures the piece at x_pos, y_pos on the board, returns
    # the captured piece that was at x_pos, y_pos, now with captured flag
    # and cur_x_pos, cur_y_pos set to _INT_BOARDSIZE to represent being off the board.
    def capture_piece(self, x_pos, y_pos, pc_attacker):
        piece = self._board[x_pos][y_pos].get_piece()

        # check that there is a piece to capture
        if piece and not piece.bln_captured:
            # replace piece on space with capturing piece
            self._board[x_pos][y_pos].occupy(pc_attacker)
            # tell the captured piece that it is off the board.
            piece.int_cur_x_pos = _INT_BOARDSIZE
            piece.int_cur_y_pos = _INT_BOARDSIZE

        return piece

    # attempts to move piece at x_s, y_s to x_d, y_d. Returns false if no piece
    #  at x_s, y_s or invalid move,
    # none if move successful and nothing to capture, or captured piece if move captures
    # piece at x_d, y_d
    def move_piece(self, x_s, y_s, x_d, y_d):
        attacker = self._board[x_s][y_s].get_piece()
        captured = None

        # check invalid starting space
        if not attacker:
            return False

        valid = self.validate_move(x_s, y_s, x_d, y_d)

        # check invalid end space
        if not valid:
            return False

        elif valid and self._board[x_d][y_d].is_occupied():
            # There is a piece to capture
            captured = self.capture_piece(x_d, y_d, attacker)
        elif valid:
            self._board[x_d][y_d].occupy(attacker)

        # update attacker on new position and return captured
        attacker.move(x_d, y_d)
        self._board[x_s][y_s].vacate()
        return captured

    # returns a list [valid, valid_moves] given source x and source y and optional
    # destination x and destination y. First entry of list determines if destination
    # is a valid destination, if given destination. Otherwise it should be ignored.
    def get_valid_moves(self, s_x, s_y, d_x=0, d_y=0):
        piece = self._board[s_x][s_y].get_piece()
        valid_moves = []
        if piece:
            possible_moves = piece.possible_moves()  # by movement rules for piece
            piece_type = type(piece).__name__  # determine which piece

            # case pawn
            if piece_type == "Pawn":
                for path in possible_moves[:-1]:
                    # check for blocking pieces
                    for space in path:
                        x = space[0]
                        y = space[1]
                        if self._board[x][y].is_occupied():
                            continue
                        else:
                            valid_moves.append([x, y])

                # check attack spaces
                attack_Squares = possible_moves[-1]
                for i in range(len(attack_Squares)):
                    x = attack_Squares[i][0]
                    y = attack_Squares[i][1]
                    bln_occupied = self._board[x][y].is_occupied()
                    # check if target space is occupied
                    if bln_occupied:
                        str_tar = self._board[x][y].get_piece().str_color
                        if str_tar == piece.str_color:
                            # space is occupied by same color piece, skip
                            continue
                        else:
                            valid_moves.append([x, y])
                    else:
                        continue

            # Note: The king can move themselves into check. Will change later.
            elif piece_type in ["Bishop", "Knight", "Rook", "Queen"]:
                for path in possible_moves:
                    for space in path:
                        x = space[0]
                        y = space[1]
                        # Blocked by piece of same color
                        if (
                            self._board[x][y].is_occupied()
                            and self._board[x][y].get_piece().str_color == piece.str_color
                        ):
                            break
                        # End path by piece of opposite collor
                        elif self._board[x][y].is_occupied():
                            valid_moves.append([x, y])
                            break
                        # Space unoccupied
                        else:
                            valid_moves.append(space)
            elif piece_type == "King":
                lst_danger_zone = get_dangerous_spaces(piece)
                for path in possible_moves[:-1]:
                    for space in path:
                        x = space[0]
                        y = space[1]
                        # Blocked by piece of same color
                        if (
                            self._board[x][y].is_occupied()
                            and self._board[x][y].get_piece().str_color == piece.str_color
                        ):
                            break
                        # End path by piece of opposite collor
                        elif self._board[x][y].is_occupied():
                            valid_moves.append([x, y])
                            break
                        # Space unoccupied
                        else:
                            valid_moves.append(space)
                # Check castling spaces for potential castling request
                castle = possible_moves[-1]
                if castle:
                    # There are possible castling moves. First is East, second West.
                    # Check East and West are clear and safe
                    # check East
                    bool_east_clear = True
                    for i in range(int(_INT_BOARDSIZE/4)):
                        if self._board[s_x+i+1][s_y].is_occupied() or ():
                            bool_east_clear = False
                            break
                        elif [s_x+i+1, s_y] in lst_danger_zone:
                            # This space is in the danger zone
                            bool_east_clear = False
                            break
                    # Now check West
                    bool_west_clear = True
                    for i in range(int(_INT_BOARDSIZE/4)):
                        if self._board[s_x+i-2][s_y].is_occupied():
                            bool_west_clear = False
                            break
                        elif [s_x+i+1, s_y] in lst_danger_zone:
                            # This space is in the danger zone
                            bool_east_clear = False
                            break
                    # Check if rooks have moved
                    bool_east_rook = False
                    if self._board[_INT_BOARDSIZE][s_y].is_occupied():
                        pc_east_rook = self._board[_INT_BOARDSIZE][s_y].get_piece(
                        )
                        bool_east_move = pc_east_rook.bln_moved
                        if not bool_east_move:
                            bool_east_rook = True
                        else:
                            # Cannot castle to the East.
                            a = 1
                    else:
                        # East Rook has moved. Do nothing.
                        a = 1
                    bool_west_rook = False
                    if self._board[0][s_y].is_occupied():
                        pc_west_rook = self._board[0][s_y].get_piece()
                        bool_west_move = pc_west_rook.bln_moved
                        if not bool_east_move:
                            bool_west_rook = True
                        else:
                            # Cannot castle to the West.
                            a = 1
                    else:
                        # West Rook has moved. Do nothing.
                        a = 1
                else:
                    # No castling moves. Do nothing.
                    a = 1
            else:
                print("validate_move case match error")
                return [False, valid_moves]
        # Now check if the given destination space is in the valid moves
        if [d_x, d_y] in valid_moves:
            return [True, valid_moves]
        else:
            return [False, valid_moves]

    # returns a list of spaces threatened by a given piece. This function operates like
    # get_valid_moves except that it will not count castling moves among the spaces
    # threatened by this piece and there is no move to check validity of.
    def get_spaces_threatened(self, piece):
        s_x = piece.int_cur_x_pos
        s_y = piece.int_cur_y_pos

        threatens = []
        if piece:
            possible_moves = piece.possible_moves()  # by movement rules for piece
            piece_type = type(piece).__name__  # determine which piece

            # case pawn
            if piece_type == "Pawn":
                for path in possible_moves[:-1]:
                    # check for blocking pieces
                    for space in path:
                        x = space[0]
                        y = space[1]
                        if self._board[x][y].is_occupied():
                            continue
                        else:
                            threatens.append([x, y])

                # check attack spaces
                attack_Squares = possible_moves[-1]
                for i in range(len(attack_Squares)):
                    x = attack_Squares[i][0]
                    y = attack_Squares[i][1]
                    bln_occupied = self._board[x][y].is_occupied()
                    # check if target space is occupied
                    if bln_occupied:
                        str_tar = self._board[x][y].get_piece().str_color
                        if str_tar == piece.str_color:
                            # space is occupied by same color piece, skip
                            continue
                        else:
                            threatens.append([x, y])
                    else:
                        continue

            # Note: The king can move themselves into check. Will change later.
            elif piece_type in ["Bishop", "Knight", "Rook", "Queen"]:
                for path in possible_moves:
                    for space in path:
                        x = space[0]
                        y = space[1]
                        # Blocked by piece of same color
                        if (
                            self._board[x][y].is_occupied()
                            and self._board[x][y].get_piece().str_color == piece.str_color
                        ):
                            break
                        # End path by piece of opposite collor
                        elif self._board[x][y].is_occupied():
                            threatens.append([x, y])
                            break
                        # Space unoccupied
                        else:
                            threatens.append(space)
            elif piece_type == "King":
                for path in possible_moves[:-1]:
                    for space in path:
                        x = space[0]
                        y = space[1]
                        # Blocked by piece of same color
                        if (
                            self._board[x][y].is_occupied()
                            and self._board[x][y].get_piece().str_color == piece.str_color
                        ):
                            break
                        # End path by piece of opposite collor
                        elif self._board[x][y].is_occupied():
                            threatens.append([x, y])
                            break
                        # Space unoccupied
                        else:
                            threatens.append(space)
            else:
                print("get_spaces_threatened case match error")
                return [False, threatens]
        # threatens now has all threatened spaces (hopefully).
        return threatens

    # Returns a list of spaces which are dangerous for a given piece, i.e. moving onto one
    # of these spaces could result in the piece being captured in the next players turn.
    def get_dangerous_spaces(self, piece):
        str_op_color = get_opposing_color(piece)
        lst_threatened = []

        # get spaces threatened by each opposing piece on the board.
        # Note that these "spaces" are list of coordinates on board,
        # not object space.
        for item in self._lst_of_pieces:
            if item.str_color == str_op_color and not item.bln_captured:
                threatens = get_spaces_threatened(item)
                for path in threatens:
                    for space in path:
                        if not (space in lst_threatened):
                            lst_threatened.append(space)
                        else:
                            continue

        # return dangerous spaces
        return lst_threatened
