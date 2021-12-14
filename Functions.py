import pygame
import Classes

import Global_variable as G

pygame.init()


def move_object(object, dude):
    """
    универсальная функция, отвечающая за движение любых объектов
    """
    object.x += object.dx - dude.dx
    object.y += object.dy
    return object

def motion_processing(object, dude):
    if (object.x + object.width <= dude.car.x + dude.dx) and (object.x + object.width + object.dx > dude.car.x +
            dude.dx) and (object.y + object.dy < dude.car.y + object.height) and (
            object.y < dude.car.y + object.height):
        object.x = dude.car.x - object.width
    elif (object.x >= dude.car.x + dude.dx + 40) and (object.x + object.dx < dude.car.x + dude.dx + 40) and (
            object.y < dude.car.y + object.height) and (object.y + object.dy < dude.car.y + object.height):
        object.x = dude.car.x + 40
        object.y += object.dy
    elif (object.y >= dude.car.y + object.height) and (object.y + object.dy < dude.car.y + object.height) and (
            dude.car.x - object.width <= object.x + object.dx - dude.dx <= dude.car.x + 40):
        object.x += object.dx - dude.dx
        object.y = dude.car.y + object.height
    else:
        object = move_object(object, dude)
    return object


def move_bullet(object):
    """
    универсальная функция, отвечающая за движение любых объектов
    """
    object.x += object.dx
    object.y += object.dy
    return object


def draw_object(object):
    """
    универсальная функция, отвечающая за прорисовку объекта на экране
    """
    G.screen.blit(object.image, (object.x, object.y))




def handle_events(event, shop_open, finished):
    """
    функция, обрабатывающая все произошедшие за временной интервал события
    """
    if event.type == pygame.QUIT:  # выхода из игры
        finished = True
    if event.type == pygame.MOUSEBUTTONDOWN:  # нажатие на кнопку мыши
        x = pygame.mouse.get_pos()[0]  # определяем координаты положения мыши
        y = pygame.mouse.get_pos()[1]
        if (x > 1100) and (y < 50):  # нажатие на кнопку магазина
            shop_open = not shop_open
    return shop_open, finished


def checking_of_repairing(repair_level, result, finished):
    if repair_level >= 500:
        result = 'ПОБЕДА'
        finished = True
    return result, finished


def create_label(label: str, size: int, a: int, b: int, border: bool, fill: bool, color: tuple):
    """
    создает надпись на заданной поверхности
    label - надпись
    size - размер шрифта
    a, b - размеры поверхности
    border - наличие рамки у пов-сти (логическая переменная)
    fill - заливка пов-сти (логическая переменная)
    color - цвет пов-сти
    """
    f = pygame.font.SysFont(None, size)
    text = f.render(label, False, G.BLACK)
    surf = pygame.Surface((a, b), pygame.SRCALPHA)
    if border:
        pygame.draw.rect(surf, G.BLACK, (0, 0, a, b), 1)
    if fill:
        pygame.draw.rect(surf, color, (0, 0, a, b), 0)
    surf.blit(text, (0, 0))
    return surf


def shop_actions(event, shop, Dude):
    if event.type == pygame.MOUSEBUTTONDOWN:  # нажатие на кнопку мыши
        x = pygame.mouse.get_pos()[0]  # определяем координаты положения мыши
        y = pygame.mouse.get_pos()[1]
        for i in range(10):
            if (shop['image'].x + shop['guns'][i]['image'].x < x < shop['image'].x + shop['guns'][i]['image'].x \
                + 250) and (
                    shop['image'].y + shop['guns'][i]['image'].y -30 < y < shop['image'].x + shop['guns'][i] \
                        ['image'].y + 30):
                continue
    return Dude

def check(check1, check2):
    if check1 or check2:
        return True
    else:
        return False


def choose(check1, check2):
    if check1:
        return 0
    if check2:
        return 1