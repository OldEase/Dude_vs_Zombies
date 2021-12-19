import pygame
import Global_variable as G
import Classes as C
import Surfaces as S
import Functions as F
from Zombies_class import Zombie
from Zombies_class import Rabbit
from random import randint


def create_shop():
    '''
    создает магазин как элемент игры
    '''
    names_of_guns = ['        PISTOL', '       REVOLVER', '     WINCHESTER', '            UZI', '       MOSSBERG',
    '          AK-47', '          M16', '       STRIKER', '        SPITFIRE', '       MINIGUN']
    cost_of_guns = [i * 500 + 1000 for i in range(8)]
    cost_of_guns[0] = '  IN USE'
    guns_button = [{'name': 0, 'image': 0, 'cost': 0} for j in range(8)]
    for i in range(5):
        guns_button[i]['name'] = C.ButtonObjects(250 * (i % 3), 160 * (i // 3),
        F.create_label(str(names_of_guns[i]),  30, 200, 30, False, True, G.YELLOW))
        guns_button[i]['image'] = C.ButtonObjects(250 * (i % 3), 160 * (i // 3) + 30, S.image_of_gun[i])
        guns_button[i]['cost'] = C.ButtonObjects(250 * (i % 3), 160 * (i // 3) + 120, F.create_label
        ('            ' + str(cost_of_guns[i]), 30, 200, 30, False, True, G.YELLOW))
        for el in guns_button[i].values():
            S.shop_window.blit(el.image, (el.x, el.y))
    image = C.ButtonObjects(225, 100, S.shop_window)
    shop = {'guns': guns_button, 'costs': cost_of_guns, 'image': image, 'open': False}
    return shop


def spawn_checking(zombies: list, dude, spawn_time: int,
                   spawn_check: bool, spawn_counter: int,
                   spawn_dif: int, spawn_cooldown: int,
                   time: int
                   ):
    '''
    отвечает за создание новых поколений зомби
    '''
    if len(zombies) == 0:
        spawn_time += 1
        if (spawn_time >= 2000) or (time == 0):
            spawn_check = True
    if spawn_check:
        if spawn_cooldown == 0:
            zombies.append(Zombie(S.width_of_images['zombie'],
                                  S.width_of_images['zombie'],
                                  'hp', dude,randint(0, 1) * 1400 - 100,
                                  350, randint(5, 8) / G.FPS * 30,
                                  10, 10, 10, 1, 100,
                                  S.new_zombie_surface()
                                  )
                           )
            zombies.append(Rabbit(S.width_of_images['rabbit'],
                                  S.width_of_images['rabbit'],
                                  'hp', dude, randint(0, 1) * 1400 - 100,
                                  388,5 / G.FPS * 30, 15 / G.FPS * 30,
                                  3, 10, 1, 1, S.surface_of_rabbit_left
                                  )
                           )
            spawn_cooldown = 144 * 3
            spawn_counter += 2
        else:
            spawn_cooldown -= 1
        if spawn_counter >= spawn_dif:
            spawn_check = False
            spawn_dif += 1
            spawn_counter = 0
    return zombies, spawn_time, spawn_check, spawn_counter, spawn_dif, spawn_cooldown







