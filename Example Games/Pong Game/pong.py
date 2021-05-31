import pygame
from pygame import*
import sys
from paddle import Paddle

pygame.init()

# game variables
black = (0,0,0)
white = (255,255,255)
size = (800,600)
game_display = pygame.display.set_mode(size)
pygame.display.set_caption('pong')

paddle1 = Paddle(white, 10, 100)
paddle1.rect.x = 25
paddle1.rect.y = 250

paddle2 = Paddle(white, 10, 100)
paddle2.rect.x = 765
paddle2.rect.y = 250

# for game's time
clock = pygame.time.Clock()

game_on = True

sprites_list = pygame.sprite.Group()

sprites_list.add(paddle1)
sprites_list.add(paddle2)

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_W]:
        paddle1.paddles_moving_up(7)

    if keys[pygame.K_S]:
        paddle1.paddles_moving_down(7)

    if keys[pygame.K_UP]:
        paddle2.paddles_moving_up(7)

    if keys[pygame.K_DOWN]:
        paddle2.paddles_moving_down(7)

    sprites_list.update()
    game_display.fill(black)

    pygame.draw.line(game_display, white, [400,0], [400,600], 5)
    sprites_list.draw(game_display)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
