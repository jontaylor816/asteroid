import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p1 = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
    game_clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        p1.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000.0
    
    

if __name__ == "__main__":
    main()
