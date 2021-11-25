import pygame as pg
from pygame.draw import *
from random import randint
import numpy as np


FPS = 60
screen_size = (1200, 900)
min_radius = 10
max_radius = 100
min_side_lenght = 40
max_side_lenght = 80
min_speed = 20
max_speed = 80
ball_number = 5
triangle_number = 5
timer = 0
time_interval = 1 / FPS

YELLOW = (100, 87, 0)
BLACK = (0, 0, 0)
COLOURS = [YELLOW]

def new_ball():
    global ball_x, ball_y, radius, ball_speed_x, ball_speed_y
    ball_x = randint(max_radius, screen_size[0] - max_radius)
    ball_y = randint(max_radius, screen_size[1] - max_radius)
    radius = randint(min_radius, max_radius)
    colour = COLOURS[randint(0, len(COLOURS) - 1)]
    ball_speed_x = randint(-max_speed, max_speed)
    ball_speed_y = randint(-max_speed, max_speed)
    circle(screen, colour, (ball_x, ball_y), radius)
    circle(screen, BLACK, (ball_x, ball_y), radius, 1)
    return ball_x, ball_y, radius, ball_speed_x, ball_speed_y


def new_triangle():
    global triangle_x1, triangle_y1, triangle_x2, triangle_y2, triangle_x3, triangle_y3,\
           side_lenght, triangle_speed_x, triangle_speed_y
    triangle_x1 = randint(0, screen_size[0] - max_side_lenght)
    triangle_y1 = randint(0, screen_size[1] - int(max_side_lenght * 3**(1 / 2) / 2))
    side_lenght = randint(min_side_lenght, max_side_lenght)
    triangle_x2 = triangle_x1 + side_lenght
    triangle_y2 = triangle_y1
    triangle_x3 = (triangle_x1 + side_lenght) / 2
    triangle_y3 = triangle_y1 + side_lenght * 3**(1 / 2) / 2
    colour = COLOURS[randint(0, len(COLOURS) - 1)]
    triangle_speed_x = randint(-max_speed, max_speed)
    triangle_speed_y = randint(-max_speed, max_speed)
    polygon(screen, colour, [(triangle_x1, triangle_y1), (triangle_x2, triangle_y2), (triangle_x3, triangle_y3)])
    polygon(screen, BLACK, [(triangle_x1, triangle_y1), (triangle_x2, triangle_y2), (triangle_x3, triangle_y3)], 1)


def ball_wall_bump():
    if ball_x < radius:
        ball_speed_x = abs(ball_speed_x)
    elif ball_x > screen_size[0] - radius:
        ball_speed_x = -abs(ball_speed_x)
    if ball_y < radius:
        ball_speed_y = abs(ball_speed_y)
    elif ball_y > screen_size[1] - radius:
        ball_speed_y = -abs(ball_speed_y)



def triangle_wall_bump():
    global triangle_speed_x, triangle_speed_y
    if triangle_x1 < side_lenght:
        triangle_speed_x = abs(triangle_speed_x)
    elif triangle_x2 > screen_size[0]:
        triangle_speed_x = -abs(triangle_speed_x)
    if triangle_y1 < side_lenght * 3**(1 / 2) / 2:
        triangle_speed_y = abs(triangle_speed_y)
    elif triangle_y3 > screen_size[1]:
        triangle_speed_y = -abs(triangle_speed_y)

def check_ball_push(event):
    if (event.pos[0] - ball_x)**2 + (event.pos[1] - ball_y)**2 <= radius**2:
        return True


def check_triangle_push(event):
    s1 = np.sign((triangle_x1 - event.pos[0]) * (triangle_y2 - triangle_y1) - (triangle_x2 - triangle_x1) *
                 (triangle_y1 - event.pos[1]))
    s2 = np.sign((triangle_x2 - event.pos[0]) * (triangle_y3 - triangle_y2) - (triangle_x3 - triangle_x2) *
                 (triangle_y2 - event.pos[1]))
    s3 = np.sign((triangle_x3 - event.pos[0]) * (triangle_y1 - triangle_y3) - (triangle_x1 - triangle_x3) *
                 (triangle_y3 - event.pos[1]))
    if s1 == s2 == s3:
        return True
    elif s1 == 0 or s2 == 0 or s3 == 0:
        return True


pg.init()
screen = pg.display.set_mode(screen_size)
pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    timer += 1
    if timer >= 15:
        finished = True
    for i in range(ball_number):
        new_ball()
        ball_wall_bump()
        ball_x += ball_speed_x * time_interval
        ball_y += ball_speed_y * time_interval

    for event in pg.event.get():
       if event.type == pg.QUIT:
           finished = True
    new_ball()
    pg.display.update()

pg.quit()

print('программа завершена')