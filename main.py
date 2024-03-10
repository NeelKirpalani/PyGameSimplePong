# Pong Game By Neel Kirpalani
# 10/3/2024 (10th March, 2024)
import pygame
import random
import sys

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set the screen size
screen = pygame.display.set_mode((800, 600))
# Set the title of the window
pygame.display.set_caption("Pong Game by Neel Kirpalani")

# Set the colors (RGB)
white = (255, 255, 255)
black = (0, 0, 0)

# Set the paddles
paddle1 = pygame.Rect(50, 250, 20, 100)
paddle2 = pygame.Rect(730, 250, 20, 100)

# Set the ball
ball = pygame.Rect(400, 300, 20, 20)

# Set the ball speed
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

# Set the paddles speed
paddle1_speed = 0
paddle2_speed = 0

# Set the score
player1_score = 0
player2_score = 0

# Set the font
font = pygame.font.Font(None, 50)

# Set the game loop
running = True

while running:
    # Set the background color
    screen.fill(black)
    # Set the paddles color
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)
    pygame.draw.rect(screen, white, ball)
    # Get the Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Keys to move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        paddle1.y += 8
    if keys[pygame.K_w]:
        paddle1.y -= 8
    if keys[pygame.K_DOWN]:
        paddle2.y += 8
    if keys[pygame.K_UP]:
        paddle2.y -= 8
    # Set the ball movement 
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # Set the ball collision
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y *= -1
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1
    if ball.left <= 0:
        player2_score += 1
        ball.center = (400, 300)
    if ball.right >= 800:
        player1_score += 1
        ball.center = (400, 300)

    # Render the scores
    player1_score_text = font.render(str(player1_score), True, white)
    player2_score_text = font.render(str(player2_score), True, white)   
    
    # Draw the scores on the screen
    screen.blit(player1_score_text, (350, 40))
    screen.blit(player2_score_text, (430, 40))

    pygame.display.update()
    # Set Frame Rate to 60
    clock.tick(60) 

pygame.quit()