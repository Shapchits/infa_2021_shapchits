import pygame as pg
from pygame.draw import *



def draw_picture(screen, x, y, width, height):
    """

    :param screen: дисплей pygame, на котором будет изображение
    :param x: левая координата прямоугольника с рисунком
    :param y: верхняя координата прямоугольника с рисунком
    :param width: ширина прямоугольника
    :param height: высота прямоугольника
    :return: рисует картинку
    """
    print('Рисую картинку.', x, y, width, height)

    draw_background(screen, x, y, width, height)

    people_x = width // 2
    people_y = height * 5 // 6
    people_height = height * 2 // 3

    draw_people(screen, people_x, people_y, people_height)

    icecream_x = width // 6
    icecream_y = height * 7 // 12
    icecream_size = people_height // 4

    balloon_size = people_height // 2
    draw_icecream(screen, icecream_x, icecream_y, icecream_size)

    balloon_x = width * 5 // 6
    balloon_y = height // 6
    balloon_size = icecream_size
    draw_balloon(screen, 'heart', balloon_x, balloon_y, balloon_size)


def draw_background(screen, x, y, width, height):
    rect(screen, BLUE, (0, 0, width, height // 2))
    rect(screen, GREEN, (0, height // 2, width, height))
    print('Рисую фон:', x, y, width, height)


def draw_people(screen, x, y, height):
    print('Рисую людей:', x, y, height)


def draw_icecream(screen, icecream_x, icecream_y, icecream_size):
    sc1 = pg.Surface((80, 80)).convert_alpha()
    pg.draw.polygon(sc1, YELLOW, ((40, 80), (20, 40), (60, 40)))
    pg.draw.circle(sc1, BROWN, (30, 30), 12)
    pg.draw.circle(sc1, RED, (50, 30), 12)
    pg.draw.circle(sc1, WHITE, (40, 20), 12)
    pg.transform.scale(sc1, (icecream_size, icecream_size))
    pg.transform.rotate(sc1, 30)
    screen.blit(sc1, (icecream_x, icecream_y))
    print('Мороженое добавлено')



def draw_balloon(screen, shape, x, y, size):
    sc2 = pg.Surface((80, 180)).convert_alpha()
    pg.draw.aaline(sc2, BLACK, (40, 180), (40, 80))
    if shape == 'heart':
        pg.draw.polygon(sc2, RED, ((40, 80), (20, 40), (60, 40)))
        pg.draw.circle(sc2, RED, (30, 40), 10)
        pg.draw.circle(sc2, RED, (50, 40), 10)
    elif shape == 'ice-cream':
        pg.draw.polygon(sc2, YELLOW, ((40, 80), (20, 40), (60, 40)))
        pg.draw.circle(sc2, BROWN, (30, 30), 12)
        pg.draw.circle(sc2, RED, (50, 30), 12)
        pg.draw.circle(sc2, WHITE, (40, 20), 12)
    pg.transform.scale(sc2, (size, int(2.25 * size)))



    print('Рисую шар:')


pg.init()
width, height = screen_size = (300, 200)
BLUE = (0, 0, 150)
GREEN = (0, 150, 0)
BLACK = (0, 0, 0)
YELLOW = (245, 207, 17)
BROWN = (120, 65, 2)
RED = (245, 23, 7)
WHITE = (255, 255, 255)
angle = 0
screen = pg.display.set_mode(screen_size)

# Здесь будем рисовать
draw_picture(screen, 0, 0, width, height)
pg.display.update()

work_flag = True
while work_flag:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            work_flag = False

print('Программа благополучно завершена.')
