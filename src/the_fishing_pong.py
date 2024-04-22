import pygame
import sys

def init_screen(resolution):
    # Used to setup the screen
    pygame.init()
    screen = pygame.display.set_mode((resolution[0], resolution[1]))
    pygame.display.set_caption('The Fishing-Pong')
    return screen

def ball_velocity(ball_pos, ball_speed, ball_size, resolution):
    # Calculates the ball's position and direction
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[0] <= 0 or ball_pos[0] >= resolution[0] - ball_size:
        ball_speed[0] = -ball_speed[0]

    if ball_pos[1] <= 0 or ball_pos[1] >= resolution[1] - ball_size:
        ball_speed[1] = -ball_speed[1]
    
    return ball_pos, ball_speed

def main():
    # Screen setup
    resolution = (800, 600)
    screen = init_screen(resolution)
    clock = pygame.time.Clock()

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Initial gameplay values
    ball_size = 30
    ball_pos = [resolution[0] // 2, resolution[1] // 2]
    ball_speed = [5, 5]

    while True:
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calculate ball position
        ball_pos, ball_speed = ball_velocity(ball_pos, ball_speed, ball_size, resolution)

        # Draw all game elements
        screen.fill(black)
        pygame.draw.ellipse(screen, white, pygame.Rect(ball_pos[0], ball_pos[1], ball_size, ball_size))
        pygame.display.flip()

        clock.tick(60) 

if __name__ == "__main__":
    main()