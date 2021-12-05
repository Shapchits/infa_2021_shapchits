import pygame as pg
from pygame.draw import *
from random import randint

FPS = 60
screen_size = (900, 600)
timer = 0
time_interval = 1 / FPS
ball_number = 5

YELLOW = (217, 173, 0)
PURPLE = (198, 134, 217)
GREEN = (117, 176, 77)
BACKGROUND = (132, 217, 210)
KEY = (100, 100, 100)
BLACK = (0, 0, 0)
COLOURS = [YELLOW, PURPLE, GREEN]


class Ball(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.min_radius = 20
        self.max_radius = 100
        self.min_speed = 65
        self.max_speed = 130
        self.radius = randint(self.min_radius, self.max_radius)
        self.ball_speed_x = randint(self.min_speed, self.max_speed)
        self.ball_speed_y = randint(self.min_speed, self.max_speed)
        self.image = pg.Surface([2 * self.radius, 2 * self.radius])
        self.image.fill(KEY)
        color = COLOURS[randint(0, len(COLOURS) - 1)]
        circle(self.image, color, (self.radius, self.radius), self.radius)
        circle(self.image, BLACK, (self.radius, self.radius), self.radius, 1)
        self.image.set_colorkey(KEY)
        self.rect = self.image.get_rect(center=(randint(self.max_radius, screen_size[0] - self.max_radius),
                                                randint(self.max_radius, screen_size[1] - self.max_radius)))

    def update(self, screen_size, time_interval):
        if self.rect.x <= 0:
            self.ball_speed_x = abs(self.ball_speed_x)
        elif self.rect.x >= screen_size[0] - 2 * self.radius:
            self.ball_speed_x = -abs(self.ball_speed_x)
        if self.rect.y <= 0:
            self.ball_speed_y = abs(self.ball_speed_y)
        elif self.rect.y >= screen_size[1] - 2 * self.radius:
            self.ball_speed_y = -abs(self.ball_speed_y)
        self.rect.x += self.ball_speed_x * time_interval
        self.rect.y += self.ball_speed_y * time_interval

    def ball_push(self, event, balls):
        if (event.pos[0] - (self.rect.x + self.radius)) ** 2 + \
                (event.pos[1] - (self.rect.y + self.radius)) ** 2 <= self.radius ** 2:
            self.kill()
            balls.add(Ball())


if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode(screen_size)
    pg.display.update()
    clock = pg.time.Clock()
    finished = False

    balls = pg.sprite.Group()
    for i in range(ball_number):
        balls.add(Ball())

    while not finished:
        clock.tick(FPS)
        timer += 1
        if timer >= 3000:
            finished = True

        for event in pg.event.get():
            if event.type == pg.QUIT:
                 finished = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                for ball in balls:
                    ball.ball_push(event, balls)

        screen.fill(BACKGROUND)
        balls.draw(screen)
        pg.display.update()

        balls.update(screen_size, time_interval)
