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

    people_x = width // 4
    people_y = height // 6
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
    image = pg.Surface((100, 90))
    image.fill(KEY)
    pg.draw.lines(image, BLACK, False, [(25, 60), (15, 85), (10, 85)])  # левая нога мальчика
    pg.draw.lines(image, BLACK, False, [(30, 60), (40, 85), (45, 85)])  # правая нога мальчика
    pg.draw.ellipse(image, VIOLET, [(15, 20), (25, 47)])
    pg.draw.circle(image, SKIN, (27, 13), 10)
    pg.draw.aaline(image, BLACK, (35, 25), (50, 55)) # правая рука мальчика
    pg.draw.aaline(image, BLACK, (20, 25), (5, 55)) # левая рука мальчтка
    pg.draw.polygon(image, PINK, [(75, 20), (90, 65), (60, 65)])
    pg.draw.circle(image, SKIN, (75, 13), 10)
    pg.draw.aaline(image, BLACK, (71, 26), (50, 55)) # левая рука девочик
    pg.draw.lines(image, BLACK, False, [(77, 26), (85, 40), (95, 30)]) # правая рука девочки
    pg.draw.lines(image, BLACK, False, [(70, 65), (70, 85), (65, 85)]) # левая нога девочки
    pg.draw.lines(image, BLACK, False, [(80, 65), (80, 85), (85, 85)]) # правая нога девочки
    pg.transform.scale(image, (height, height))
    image.set_colorkey(KEY)
    image = pg.transform.scale(image, [height, height])
    screen.blit(image, (x, y))

    print('Рисую людей:', x, y, height)


def draw_icecream(screen, icecream_x, icecream_y, icecream_size):
    image = pg.Surface((80, 80))
    image.fill(KEY)
    pg.draw.polygon(image, YELLOW, ((40, 80), (20, 40), (60, 40)))
    pg.draw.circle(image, BROWN, (30, 30), 12)
    pg.draw.circle(image, RED, (50, 30), 12)
    pg.draw.circle(image, WHITE, (40, 20), 12)
    image.set_colorkey(KEY)
    image = pg.transform.scale(image, (icecream_size, icecream_size))
    image = pg.transform.rotate(image, 30)
    screen.blit(image, (icecream_x, icecream_y))
    print('Мороженое добавлено')



def draw_balloon(screen, shape, x, y, size):
    image = pg.Surface((80, 160))
    image.fill(KEY)
    pg.draw.line(image, BLACK, (40, 160), (40, 80), width=2)
    if shape == 'heart':
        pg.draw.polygon(image, RED, ((40, 80), (20, 40), (60, 40)))
        pg.draw.circle(image, RED, (30, 40), 10)
        pg.draw.circle(image, RED, (50, 40), 10)
    elif shape == 'ice-cream':
        pg.draw.polygon(image, YELLOW, ((40, 80), (20, 40), (60, 40)))
        pg.draw.circle(image, BROWN, (30, 30), 12)
        pg.draw.circle(image, RED, (50, 30), 12)
        pg.draw.circle(image, WHITE, (40, 20), 12)
    image.set_colorkey(KEY)
    image = pg.transform.scale(image, (size, int(2.25 * size)))
    image = pg.transform.rotate(image, -20)
    screen.blit(image, (x, y))



    print('Рисую шар:')


pg.init()
width, height = screen_size = (300, 200)
BLUE = (142, 225, 250)
GREEN = (74, 168, 112)
BLACK = (0, 0, 0)
YELLOW = (245, 207, 17)
BROWN = (120, 65, 2)
RED = (245, 23, 7)
WHITE = (255, 255, 255)
SKIN = (252, 223, 179)
VIOLET = (156, 103, 161)
PINK = (245, 122, 233)
KEY = (100, 100, 100)
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

