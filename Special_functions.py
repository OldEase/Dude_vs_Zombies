import pygame
import Global_variable as G
import Classes as C
import Surfaces as S
import Functions as F
from Zombies_class import Zombie
from random import randint


def create_shop():
    names_of_guns = ['        PISTOL', '       REVOLVER', '     WINCHESTER', '            UZI', '       MOSSBERG',
    '          AK-47', '          M16', '       STRIKER', '        SPITFIRE', '       MINIGUN']
    cost_of_guns = [i * 500 + 1000 for i in range(10)]
    cost_of_guns[0] = '  IN USE'
    guns_button = [{'name': 0, 'image': 0, 'cost': 0} for j in range(10)]
    for i in range(10):
        guns_button[i]['name'] = C.Button_objects(250 * (i % 5), 160 * (i // 5),
        F.create_label(str(names_of_guns[i]),  30, 200, 30, False, True, G.YELLOW))
        guns_button[i]['image'] = C.Button_objects(250 * (i % 5), 160 * (i // 5) + 30, S.image_of_gun)
        guns_button[i]['cost'] = C.Button_objects(250 * (i % 5), 160 * (i // 5) + 120, F.create_label
        ('            ' + str(cost_of_guns[i]), 30, 200, 30, False, True, G.YELLOW))
        for el in guns_button[i].values():
            S.shop_window.blit(el.image, (el.x, el.y))
    image = C.Button_objects(100, 100, S.shop_window)
    shop = {'guns': guns_button, 'image': image, 'open': False}
    return shop


def spaun_checking(zombies, dude, spawn_time, spawn_check, spawn_counter):
    if len(zombies) == 0:
        spawn_time += 1
        if spawn_time >= 1440:
            spawn_check = True
    if spawn_check:
        zombies.append(Zombie(S.width_of_images['zombie'], S.width_of_images['zombie'], 'hp', dude,
                randint(0, 3) * 1200 - 1800, 350, randint(2, 6) / G.FPS * 30, 10, 10, 10, 1, 1,
                                           S.surface_of_zombie_right))
        spawn_counter += 10
        if spawn_counter >= 100:
            spawn_check = False
    return zombies, spawn_time, spawn_check, spawn_counter







