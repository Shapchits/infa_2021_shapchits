import pygame as pg


def draw_picture(screen, x, y, width, height):
    """
    Рисует картинку

    : param screen: дисплей pygame, на котором будет изображение
    : param x: левая координата прямоугольника с рисунком
    : param y: верхняя координата прямоугольника с рисунком
    : param width: ширина прямоугольника
    : param height: высота прямоугольника
    """
    print('Рисую картинку.', x, y, width, height)


pg.init()
width, height = screen_size = (300, 200)
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
