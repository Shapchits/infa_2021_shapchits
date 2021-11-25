import pygame as pg
from pygame.draw import *
from random import randint
import numpy as np

FPS = 60
screen_size = (1200, 900)
timer = 0
time_interval = 1 / FPS

YELLOW = (100, 87, 0)
BLACK = (0, 0, 0)
COLOURS = [YELLOW]


class Ball(pg.sprite.Sprite):
    min_radius = 10
    max_radius = 100
    min_speed = 20
    max_speed = 80
    number = 5


    def __init__(self, min_radius, max_radius, max_speed):
        pg.sprite.Sprite.__init__(self)
        self.radius = randint(min_radius, max_radius)
        self.x = randint(max_radius, screen_size[0] - max_radius)
        self.y = randint(max_radius, screen_size[1] - max_radius)
        self.speed_x = randint(-max_speed, max_speed)
        self.speed_y = randint(-max_speed, max_speed)

    def create_ball(self, min_radius, max_radius, max_speed):
        radius = randint(min_radius, max_radius)
        x = randint(max_radius, screen_size[0] - max_radius)
        y = randint(max_radius, screen_size[1] - max_radius)
        speed_x = randint(-max_speed, max_speed)
        speed_y = randint(-max_speed, max_speed)
        return x, y, radius, speed_x, speed_y


    def draw_ball(self, x, y, radius):
        color = COLOURS[randint(0, len(COLOURS) - 1)]
        circle(screen, color, (x, y), radius)
        circle(screen, BLACK, (x, y), radius, 1)


    def wall_bump(self, x, y, radius, speed_x, speed_y):
        if x < radius:
            speed_x = abs(speed_x)
        elif x > screen_size[0] - radius:
            speed_x = -abs(speed_x)
        if y < radius:
            speed_y = abs(speed_y)
        elif y > screen_size[1] - radius:
            speed_y = -abs(speed_y)
        return speed_x, speed_y


    def check_ball_push(self, event, x, y, radius):
        if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 <= radius ** 2:
            return True


    def update(self):
        self.ball.x +=


pg.init()
screen = pg.display.set_mode(screen_size)
pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    timer += 1
    if timer >= 400:
        finished = True

    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

        ball = Ball()
        ball_list = []
        for i in range(ball.number):
            a = list(ball.create_ball(ball.min_radius, ball.max_radius, ball.max_speed))
            ball_list.append(a)
        for i in ball_list:
            ball.draw_ball(i[0], i[1], i[2])

        if event.type == pg.MOUSEBUTTONDOWN:
            for i in ball_list:
                ball.check_ball_push(event, i[0], i[1], i[2])
                if ball.check_ball_push(event, i[0], i[1], i[2]):
                    del ball_list[i]
                    new = list(ball.create_ball(ball.min_radius, ball.max_radius, ball.max_speed))
                    ball_list.append(new)
                    ball.draw_ball(new[0], new[1], new[2])
        for i in ball_list:
            i[0] += i[3] * time_interval
            i[1] += i[4] * time_interval
        pg.display.update()
        screen.fill(BLACK)

pg.quit()
