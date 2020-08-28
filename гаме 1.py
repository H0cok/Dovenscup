import pygame
from math import sqrt
import random
pygame.init()
screen = pygame.display.set_mode((1024, 600))
field = pygame.image.load("Field.png")
ballimg = pygame.image.load("ball.png")

pygame.display.set_caption("DOVENS CUP")
pygame.display.set_icon(pygame.image.load("001-soccer-field.png"))
running = True

def dist(a, b):
    return int(sqrt(a**2 + b**2))


startjumpX = 0
startjumpY = 0
jump = False
halfjump = False


player1img = pygame.image.load("pl.png")
player1X = 200
player1Y = 280
player1X_change_plus = 0
player1X_change_min = 0
player1Y_change_min =0
player1Y_change_plus = 0
player1Y_change_jump = 0

player2img = pygame.image.load("pl1rev.png")
player2X = 800
player2Y = 250


#for start 507 346
#for center enemy
ballX = 1008
ballY = 370
kickfirst = False


def player1(x, y):

    screen.blit(player1img, (x, y))

def ball(x, y):
    screen.blit(ballimg, (x, y) )

def player2(x, y):
    screen.blit(player2img, (x, y))


def kick(power, x, y, ft, typ):
    if ft == True:
        power = power * 1.5
    if typ == 1:
        return [power, power*190, random.randint(0, 420 - power*5)]





while running:
    screen.blit(field, (0, 0))
    player1(player1X, player1Y)

    player2(player2X, player2Y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player1X_change_plus = 2
            if event.key == pygame.K_LEFT:
                player1X_change_min = -2
            if event.key == pygame.K_UP:
                player1Y_change_plus = -2
            if event.key == pygame.K_DOWN:
                player1Y_change_min = 2
            if not jump:
                if event.key == pygame.K_SPACE:
                    jump = True
                    startjumpY = player1Y
                    player1Y_change_jump = -6
            if event.key == pygame.K_w:
                power = dist(ballY - player1Y - 75, ballX - player1X - 42)
                if power < 15:
                    print(kick(power, ballX, ballY, kickfirst, 1))


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player1X_change_plus = 0
            if event.key == pygame.K_LEFT:
                player1X_change_min = 0
            if event.key == pygame.K_UP:
                player1Y_change_plus = 0
            if event.key == pygame.K_DOWN:
                player1Y_change_min = 0
    if jump and startjumpY - 90 > player1Y:
        player1Y_change_jump = 4
        halfjump = True
    if jump and startjumpY -1 < player1Y and halfjump == True:
        jump = False
        halfjump = False
        player1Y_change_jump = 0
    if player1Y >= 485:
        player1Y_change_min = 0
    if player1Y < 96:
        player1Y_change_plus = 0

    player1X += player1X_change_plus + player1X_change_min
    player1Y += player1Y_change_plus + player1Y_change_min + player1Y_change_jump
    if player1X >= 448:
        player1X = 448
    if player1X <= 0:
        player1X = 0
    ball(ballX, ballY)



    pygame.display.update()
