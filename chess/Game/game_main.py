from chess.Game.game import Game
import pygame as p




WIDTH = 440
HEIGHT = 440



def main():
    p.init()
    # print(WIDTH)
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    print("Testing")
    print(screen.get_width())

    game = Game(screen)

    # game.play()
    

    game._draw_board()
    running  = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        clock.tick(15)
        p.display.flip()



main()
    
