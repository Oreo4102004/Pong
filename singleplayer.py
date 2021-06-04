import pygame, random

pygame.init()
running = True
clock = pygame.time.Clock()
pygame.display.set_caption('Ping Pong')
pygame.display.set_icon(pygame.image.load('icon.png'))


def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball.x = screen_width / 2 - 15
        ball.y = screen_height / 2 - 15
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1


def paddle_animation():
    paddle1.y += paddle_speed
    if paddle1.top <= 0:
        paddle1.top = 0
    if paddle1.bottom >= screen_height:
        paddle1.bottom = screen_height


def AI():
    if paddle2.y < ball.y:
        paddle2.y += opponent_speed
    if paddle2.y > ball.y:
        paddle2.y -= opponent_speed
    if paddle2.top <= 0:
        paddle2.top = 0
    if paddle2.bottom >= screen_height:
        paddle2.bottom = screen_height


screen_width, screen_height = 1000, 700
screen = pygame.display.set_mode((screen_width, screen_height))
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
paddle1 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
paddle2 = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
bgcolor = pygame.Color('grey12')
color = (200, 200, 200)
ball_speed_x = random.choice((1, -1))
ball_speed_y = random.choice((1, -1))
paddle_speed = 0
opponent_speed = 1
paddle1_score = 0
paddle2_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 32)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                paddle_speed += 1
            if event.key == pygame.K_UP:
                paddle_speed -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                paddle_speed -= 1
            if event.key == pygame.K_UP:
                paddle_speed += 1
    screen.fill(bgcolor)
    ball_animation()
    paddle_animation()
    AI()
    screen.fill(bgcolor)
    pygame.draw.rect(screen, color, paddle1)
    pygame.draw.rect(screen, color, paddle2)
    pygame.draw.ellipse(screen, color, ball)
    pygame.draw.aaline(screen, color, (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.display.update()
