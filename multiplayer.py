import pygame
import random
import socket

from pygame.constants import TEXTINPUT

pygame.init()
running = True
clock = pygame.time.Clock()
pygame.display.set_caption('Ping Pong')
pygame.display.set_icon(pygame.image.load('icon.png'))


class Select:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket()

    def server(self):
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        self.clientsocket, self.address = self.s.accept()
        while self.clientsocket:
            print(f"{self.address} connected")
            while True:
                self.data = self.clientsocket.recv(1024)
                if not self.data:
                    break
                print(self.data)
                self.clientsocket.sendall(paddle2)
    def client(self):
        self.s.connect((self.host,self.port))
        x=self.s.sendall(paddle1)
        print(x)
        self.s.recv(1024)

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


screen_width, screen_height = 1280, 960
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
    screen.fill(bgcolor)
    pygame.draw.rect(screen, color, paddle1)
    pygame.draw.rect(screen, color, paddle2)
    pygame.draw.ellipse(screen, color, ball)
    pygame.draw.aaline(screen, color, (screen_width / 2, 0),
                       (screen_width / 2, screen_height))
    pygame.display.update()
