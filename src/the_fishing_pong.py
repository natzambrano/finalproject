import pygame
import sys

def init_screen(resolution):
    pygame.init()
    screen = pygame.display.set_mode((resolution[0], resolution[1]))
    pygame.display.set_caption('The Fishing-Pong')
    return screen

def main():
    # Screen setup
    resolution = (800, 600)
    screen = init_screen(resolution)
    clock = pygame.time.Clock()

    # Colors
    black = (0, 0, 0)

    while True:
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)

        pygame.display.flip()

        clock.tick(60) 

if __name__ == "__main__":
    main()