import pygame as pg
from pygame.draw import *
from random import randint
pg.init()

FPS = 60
screen_size = (1200, 900)
min_radius = 10
max_radius = 100
min_ball_speed = 20
max_ball_speed = 80

YELLOW = (100, 87, 0)
COLOURS = [YELLOW]

def new_ball():
    global ball_x, ball_y, radius, ball_speed_x, ball_speed_y
    ball_x = randint(max_radius, screen_size[0] - max_radius)
    ball_y = randint(max_radius, screen_size[1] - max_radius)
    radius = randint(min_radius, max_radius)
    colour = COLOURS[randint(0, len(COLOURS) - 1)]
    ball_speed_x = randint(-max_ball_speed, max_ball_speed)
    ball_speed_y = randint(-max_ball_speed, max_ball_speed)
    circle(screen, colour, (ball_x, ball_y), radius)


def ball_wall_bump():
    if ball_x < radius:
        ball_speed_x = abs(ball_speed_x)
    elif ball_x > screen_size[0] - radius:
        ball_speed_x = -abs(ball_speed_x)
    if ball_y < radius:
        ball_speed_y = abs(ball_speed_y)
    elif ball_y > screen_size[1] - radius:
        ball_speed_y = -abs(ball_speed_y)

print('программа завершена')