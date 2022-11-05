from chess.Game.game import Game
import pygame as p
from chess.Board.board import Board




WIDTH = 440
HEIGHT = 440
SQ_SIZE = 440//8


def main():
    p.init()
    # print(WIDTH)
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    game = Game(screen)

    # game.play()
    

    game._draw_board()
    game._draw_pieces()
    running  = True
    tup_sq_selected = ()
    lst_player_clicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                tup_location = p.mouse.get_pos() # (x,y) location of mouse
                int_x_select = tup_location[0]//SQ_SIZE
                int_y_select = tup_location[1]//SQ_SIZE
                tup_sq_selected = (int_x_select, int_y_select)
                if tup_sq_selected in lst_player_clicks:
                    lst_player_clicks = []
                else:
                    lst_player_clicks.append(tup_sq_selected)

                if len(lst_player_clicks) == 2:
                    game.move_piece(lst_player_clicks)
                    lst_player_clicks = []
        clock.tick(15)
        p.display.flip()



main()
    
