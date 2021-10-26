import pygame as pg
from pygame.draw import *


def draw_picture(screen, x, y, width, height):
    draw_background(screen, x, y, width, height)

    people_x = width // 2 - height * 2 // 3 + width // 20
    people_y = height // 5
    people_height = height * 2 // 3

    draw_people(screen, people_x, people_y, people_height, reversal=False)
    draw_people(screen, width // 2, people_y, people_height, reversal=True)

    icecream_size = people_height // 4
    icecream_x = width // 2 + people_height * 4 // 5
    icecream_y = people_y - icecream_size + height // 2.7

    draw_icecream(screen, icecream_x, icecream_y, icecream_size, -30)
    draw_balloon(screen, 'ice-cream', width // 2 - people_height // 5,
                 people_y - people_height * 3 // 10, people_height // 3, 10)
    draw_balloon(screen, 'heart', people_x - people_height // 4,
                 icecream_y - people_height // 4, people_height // 4, 20)


def draw_background(screen, x, y, width, height):
    rect(screen, BLUE, (x, y, width, height // 2))
    rect(screen, GREEN, (x, height // 2, width, height))


def draw_people(screen, x, y, height, reversal):
    image = pg.Surface((100, 90))
    image.fill(KEY)
    pg.draw.lines(image, BLACK, False, [(25, 60), (15, 85), (10, 85)])  # левая нога мальчика
    pg.draw.lines(image, BLACK, False, [(30, 60), (40, 85), (45, 85)])  # правая нога мальчика
    pg.draw.ellipse(image, VIOLET, [(15, 20), (25, 47)])
    pg.draw.circle(image, SKIN, (27, 13), 10)
    pg.draw.aaline(image, BLACK, (35, 25), (50, 55)) # правая рука мальчика
    pg.draw.aaline(image, BLACK, (20, 25), (5, 55)) # левая рука мальчика
    pg.draw.lines(image, BLACK, False, [(70, 65), (70, 85), (65, 85)])  # левая нога девочки
    pg.draw.lines(image, BLACK, False, [(80, 65), (80, 85), (85, 85)])  # правая нога девочки
    pg.draw.polygon(image, PINK, [(75, 20), (90, 65), (60, 65)])
    pg.draw.circle(image, SKIN, (75, 13), 10)
    pg.draw.aaline(image, BLACK, (73, 26), (50, 55)) # левая рука девочки
    pg.draw.lines(image, BLACK, False, [(77, 26), (85, 40), (95, 30)]) # правая рука девочки
    image.set_colorkey(KEY)
    image = pg.transform.scale(image, [height, height * 9 // 10])
    if reversal:
        image = pg.transform.flip(image, True, False)
    screen.blit(image, (x, y))


def draw_icecream(screen, x, y, size, angle):
    image = pg.Surface((80, 80))
    image.fill(KEY)
    pg.draw.polygon(image, YELLOW, ((40, 80), (20, 40), (60, 40)))
    pg.draw.circle(image, BROWN, (30, 30), 12)
    pg.draw.circle(image, RED, (50, 30), 12)
    pg.draw.circle(image, WHITE, (40, 20), 12)
    image.set_colorkey(KEY)
    image = pg.transform.scale(image, (size, size))
    image = pg.transform.rotate(image, angle)
    screen.blit(image, (x, y))


def draw_balloon(screen, shape, x, y, size, angle):
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
    image = pg.transform.scale(image, (size, (2 * size)))
    image = pg.transform.rotate(image, angle)
    screen.blit(image, (x, y))


pg.init()
width, height = screen_size = (450, 300)
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

draw_picture(screen, 0, 0, width, height)
pg.display.update()

work_flag = True
while work_flag:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            work_flag = False

print('Программа благополучно завершена.')
