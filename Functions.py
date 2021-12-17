import pygame
import Classes
import numpy as np

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
    if dude.car.x - dude.width < dude.x + dude.dx < dude.car.x + dude.car.width:
        if (object.x + object.width <= dude.car.x + dude.dx) and (object.x + object.width + object.dx > dude.car.x +
                dude.dx) and (object.y + object.dy < dude.car.y + object.height) and (
                object.y < dude.car.y + object.height):
            object.x = dude.car.x - object.width
            object.y += object.dy
            dude.car.repair_level += - object.damage // 10
        elif (object.x >= dude.car.x + dude.dx + dude.car.width) and (object.x + object.dx < dude.car.x + dude.dx +
                dude.car.width) and (object.y < dude.car.y + object.height) and (object.y + object.dy < dude.car.y + object.height):
            object.x = dude.car.x + dude.car.width
            object.y += object.dy
            dude.car.repair_level += - object.damage // 10
        #elif (object.y >= dude.car.y + object.height) and (object.y + object.dy < dude.car.y + object.height) and (
                #dude.car.x - object.width <= object.x + object.dx - dude.dx <= dude.car.x + dude.car.width):
            #object.x += object.dx - dude.dx
            #object.y = dude.car.y + object.height
        else:
            object = move_object(object, dude)
    else:
        object = move_object(object, dude)
    return object, dude


def move_bullet(object):
    """
    универсальная функция, отвечающая за движение любых объектов
    """
    object.x += object.dx
    object.y += object.dy
    return object


def draw_object(object):
    """
    универсальная функция, отвечающая за прорисовку объектов на экране
    """
    G.screen.blit(object.image, (object.x, object.y))

def collision_with_zombie(zombies, dude, bullets):
    j = len(zombies) - 1
    while j >= 0:
        if (dude.x - zombies[j].width <= zombies[j].x <= dude.x + dude.width) and (dude.y > zombies[j].y -
                dude.height) and not dude.stun['fact']:
            dude.lives += - zombies[j].damage
            if dude.x - zombies[j].x == 0:
                dude.dx = dude.width * 2
            else:
                dude.dx = (dude.x - zombies[j].x) / np.abs(dude.x - zombies[j].x) * 2 * dude.width
            dude.dy = 0
            dude.stun['fact'] = True
        counter = 0
        exist_check = True
        for bull in bullets:
            inside_check = False
            if bull.x > 1300 or bull.x < -100:
                bullets.pop(counter)

            for i in range(20):
                bull = move_bullet(bull)
                if (zombies[j].mask.overlap_area(bull.mask,
                                             (int(-zombies[j].x + bull.x),
                                              int(-zombies[j].y + bull.y)))) != 0 and not inside_check:
                    (x, y) = zombies[j].mask.overlap(
                        bull.mask, (int(-zombies[j].x + bull.x), int(-zombies[j].y + bull.y)))
                    pygame.draw.rect(zombies[j].image, G.WHITE, (x, y, 2, 2))
                    pygame.draw.rect(zombies[j].image, G.RED, (x + 2 * bull.dx / abs(bull.dx), y, 1, 1))
                    zombies[j].mask = pygame.mask.from_surface(zombies[j].image)
                    zombies[j].lives += - bull.damage
                    print(zombies[j].lives, 'попал')
                    if zombies[j].lives <= 0 and exist_check:
                        zombies.pop(j)
                        print('убил')
                        exist_check = False
                        break
                    inside_check = True
                    bullets.pop(counter)
            if not inside_check:
                draw_object(bull)
            counter += 1
            if not exist_check:
                break
        j += -1
    return zombies, dude, bullets

def draw_hp(object):
    '''
    отображает на экране текущее состояние здоровья персонажа
    '''
    print(object)
    pygame.draw.rect(G.screen, G.WHITE, (object.x, object.y - 16, object.width, 8))
    pygame.draw.rect(G.screen, G.RED, (object.x, object.y - 16, object.width * object.lives // object.lives0, 8))

def checking_of_stun(dude):
    '''
    Проверяет, оглушен ли человечек в данный момент, и выполняет необходимые в данном случае действия
    '''
    if dude.stun['fact']:
        if dude.stun['time'] > 0:
            pass
            # dude.dx = 0
        dude.stun['time'] += 1
        if dude.stun['time'] >= 18:
            dude.stun['fact'], dude.stun['time'] = False, 0
    return dude


def update_live_objects(objects):
    live_objects = [objects['dude']] + objects['zombies'] + [objects['rabbit']]
    return live_objects


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


def checking_of_end(lives, repair_level, result, finished):
    if repair_level >= 5000:
        result = 'ПОБЕДА'
        finished = True
    if (repair_level) <= 0 or (lives <= 0):
        result = 'ПОРАЖЕНИЕ'
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

def check(check1, check2, check3, check4, check5):
    if check1 or check2 or check3 or check4 or check5:
        return True
    else:
        return False


def choose(check1, check2, check3, check4, check5):
    if check1:
        return 0
    if check2:
        return 1
    if check3:
        return 2
    if check4:
        return 3
    if check5:
        return 4
     