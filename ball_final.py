import pygame as pg
from pygame.draw import *
from random import randint

FPS = 60
screen_size = (900, 600)
timer = 0
time_interval = 1 / FPS
ball_number = 5
score = 0

YELLOW = (217, 173, 0)
PURPLE = (198, 134, 217)
GREEN = (117, 176, 77)
BACKGROUND = (132, 217, 210)
KEY = (100, 100, 100)
BLACK = (0, 0, 0)
COLOURS = [YELLOW, PURPLE, GREEN]


class Ball(pg.sprite.Sprite):

    def __init__(self):
        """
        Инициализирует класс Ball.
        Атрибуты:
            min_radius (int): минимально возможный радиус шара
            max_radius (int): максимально возможный радиус шара
            min_speed (int): минимально возможная скорость шара
            max_speed (int): максимально возможная скорость шара
            radius (int): радиус шара
            ball_speed_x (int): горизонтальная проекция скорости шара
            ball_speed_y (int): вертикальная проекция скорости шара
            ball_score (int): количество очков, начисляемых за попадание по шарику
            image (pg.Surface): поверхность, на которой будет изображение шара
            rect (pg.Rect): задает положение изображения шара на игровом поле
        """
        pg.sprite.Sprite.__init__(self)
        self.min_radius = 20
        self.max_radius = 100
        self.min_speed = 60
        self.max_speed = 120
        self.radius = randint(self.min_radius, self.max_radius)
        self.ball_speed_x = randint(self.min_speed, self.max_speed)
        self.ball_speed_y = randint(self.min_speed, self.max_speed)
        self.ball_score = 15
        self.image = pg.Surface([2 * self.radius, 2 * self.radius])
        self.image.fill(KEY)
        color = COLOURS[randint(0, len(COLOURS) - 1)]
        circle(self.image, color, (self.radius, self.radius), self.radius)
        circle(self.image, BLACK, (self.radius, self.radius), self.radius, 1)
        self.image.set_colorkey(KEY)
        self.rect = self.image.get_rect(center=(randint(self.max_radius, screen_size[0] - self.max_radius),
                                                randint(self.max_radius, screen_size[1] - self.max_radius)))

    def update(self, screen_size, time_interval):
        """
        Обновляет положение спрайта на игровом поле, регулирует отражение шара от стен.
        :param screen_size: размеры игрового поля
        :type screen_size: tuple
        :param time_interval: временной промежуток
        :type time_interval: float
        :return: None
        """
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
        """
        Проверяет, попал ли игрок по шарику, и в случае попадания возвращает True, удаляет данный шар и создает на
         игровом поле новый.
        :param event: событие от игрока
        :type event: Event
        :param score: число очков
        :type score: int
        :param balls: группа спрайтов
        :type balls: pygame.sprite.Group
        """
        if (event.pos[0] - (self.rect.x + self.radius)) ** 2 + \
                (event.pos[1] - (self.rect.y + self.radius)) ** 2 <= self.radius ** 2:

            self.kill()
            balls.add(Ball())
            return True


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
                    if ball.ball_push(event, balls):
                        score += ball.ball_score

        screen.fill(BACKGROUND)
        balls.draw(screen)
        pg.display.update()

        balls.update(screen_size, time_interval)
    print(score)
