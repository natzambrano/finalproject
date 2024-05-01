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

    if ball_pos[1] <= 0 or ball_pos[1] >= resolution[1] - ball_size:
        ball_speed[1] = -ball_speed[1]
    
    return ball_pos, ball_speed

def paddle(paddle1_pos, paddle2_pos, paddle_height, paddle_speed, resolution, keys_pressed):
    # Calculates the paddle movements
    if keys_pressed[pygame.K_w] and paddle1_pos[1] > 0:
        paddle1_pos[1] -= paddle_speed
    if keys_pressed[pygame.K_s] and paddle1_pos[1] < resolution[1] - paddle_height:
        paddle1_pos[1] += paddle_speed
    if keys_pressed[pygame.K_UP] and paddle2_pos[1] > 0:
        paddle2_pos[1] -= paddle_speed
    if keys_pressed[pygame.K_DOWN] and paddle2_pos[1] < resolution[1] - paddle_height:
        paddle2_pos[1] += paddle_speed
    return paddle1_pos, paddle2_pos

def reset_ball(ball_pos, ball_speed, resolution):
    # Resets the ball if going past resolution
    if ball_pos[0] < 0 or ball_pos[0] > resolution[0]:
        ball_pos = [resolution[0] // 2, resolution[1] // 2]
        ball_speed = [5, 5] if ball_speed[0] > 0 else [-5, 5]
    return ball_pos, ball_speed

def main():
    # Screen setup
    resolution = (800, 600)
    screen = init_screen(resolution)
    clock = pygame.time.Clock()
    
    # Images
    background = pygame.transform.scale(pygame.image.load("assets/background.jpg").convert(), resolution)
    salmon = pygame.transform.scale(pygame.image.load("assets/salmon.png").convert_alpha(), (80, 200))
    trout = pygame.transform.scale(pygame.image.load("assets/trout.png").convert_alpha(), (80, 200))
    bobber = pygame.transform.scale(pygame.image.load("assets/bobber.png").convert_alpha(), (30, 30))

    # Initial gameplay values
    ball_size = 30
    ball_pos = [resolution[0] // 2, resolution[1] // 2]
    ball_speed = [5, 5]
    paddle_dimension = (20, 200)
    paddle_speed = 10
    paddle1_pos = [10, resolution[1] // 2 - paddle_dimension[1] // 2]
    paddle2_pos = [resolution[0] - 10 - paddle_dimension[0], resolution[1] // 2 - paddle_dimension[1] // 2]

    while True:
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move the paddles
        paddle1_pos, paddle2_pos = paddle(paddle1_pos, paddle2_pos, paddle_dimension[1], paddle_speed, resolution, keys_pressed)
        
        # Calculate ball position
        ball_pos, ball_speed = ball_velocity(ball_pos, ball_speed, ball_size, resolution)

        # Paddle collision logic
        paddle1_collision = (
            ball_pos[0] <= paddle1_pos[0] + paddle_dimension[0] and
            paddle1_pos[1] <= ball_pos[1] <= paddle1_pos[1] + paddle_dimension[1])
        
        paddle2_collision = (
            ball_pos[0] + ball_size >= paddle2_pos[0] and
            paddle2_pos[1] <= ball_pos[1] <= paddle2_pos[1] + paddle_dimension[1])
        
        if paddle1_collision or paddle2_collision:
            ball_speed[0] = -ball_speed[0]
        
        # Reset the ball's position
        ball_pos, ball_speed = reset_ball(ball_pos, ball_speed, resolution)

        screen.blit(background, (0, 0))
        screen.blit(salmon, (paddle1_pos[0] - 20, paddle1_pos[1])) #minus 20 to center properly
        screen.blit(trout, (paddle2_pos[0] - 40, paddle2_pos[1])) #minus 40 to center properly
        screen.blit(bobber, (ball_pos[0], ball_pos[1]))
        
        pygame.display.flip()
        clock.tick(60) 

if __name__ == "__main__":
    main()