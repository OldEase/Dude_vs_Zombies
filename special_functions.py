import global_variable as g
import classes as c
import surfaces as s
import functions as f
from zombies_class import Zombie
from zombies_class import Rabbit
from random import randint


def create_shop(dude):
    """
    создает магазин как элемент игры
    """
    names_of_guns = ['        PISTOL', '       REVOLVER', '     WINCHESTER', '            UZI', '       MOSSBERG',
                     '              KIT']
    cost_of_guns = [(i + 1) % 6 * 500 + 500 for i in range(6)]
    cost_label = []
    for i in cost_of_guns:
        cost_label.append(i)
    cost_label[0] = 'IN ARSENAL'
    for i in range(6):
        if type(cost_label[i]) == int:
            if dude.money < cost_label[i]:
                cost_label[i] = 'CLOSED'
    guns_button = [{'name': 0, 'image': 0, 'cost': 0} for j in range(6)]
    for i in range(6):
        guns_button[i]['name'] = c.ButtonObjects(250 * (i % 3), 160 * (i // 3),
                                                 f.create_label(str(names_of_guns[i]), 30, 200, 30, False, True,
                                                                g.YELLOW))
        guns_button[i]['image'] = c.ButtonObjects(250 * (i % 3), 160 * (i // 3) + 30, s.image_of_gun[i])
        guns_button[i]['cost'] = c.ButtonObjects(250 * (i % 3), 160 * (i // 3) + 120, f.create_label
        ('            ' + str(cost_label[i]), 30, 200, 30, False, True, g.YELLOW))
        for el in guns_button[i].values():
            s.shop_window.blit(el.image, (el.x, el.y))
    image = c.ButtonObjects(225, 100, s.shop_window)
    shop = {'guns': guns_button, 'costs': cost_of_guns, 'cost_label': cost_label, 'image': image, 'open': False}
    return shop


def update_shop(shop, dude):
    """
    обновляет магазин
    """
    shop['image'].image.fill(g.BLACK)
    for i in range(6):
        if shop['cost_label'][i] != 'IN ARSENAL':
            if dude.money < shop['costs'][i]:
                shop['cost_label'][i] = 'CLOSED'
            else:
                shop['cost_label'][i] = shop['costs'][i]
        shop['guns'][i]['cost'] = c.ButtonObjects(250 * (i % 3), 160 * (i // 3) + 120, f.create_label
        ('            ' + str(shop['cost_label'][i]), 30, 200, 30, False, True, g.YELLOW))
        for el in shop['guns'][i].values():
            shop['image'].image.blit(el.image, (el.x, el.y))
    return shop


def spawn_checking(zombies: list, dude, spawn_time: int,
                   spawn_check: bool, spawn_counter: int,
                   spawn_dif: int, spawn_cooldown: int,
                   time: int
                   ):
    """
    отвечает за создание новых поколений зомби
    """
    if len(zombies) == 0:
        spawn_time += 1
        if (spawn_time >= 2000) or (time == 0):
            spawn_check = True
    if spawn_check:
        if spawn_cooldown == 0:
            zombies.append(Zombie(s.width_of_images['zombie'],
                                  s.width_of_images['zombie'],
                                  'hp', dude, randint(0, 1) * 1400 - 100,
                                  350, randint(3, 7) / g.FPS * 30,
                                  10, 10, 10, 1, 100,
                                  s.new_zombie_surface()
                                  )
                           )
            zombies.append(Rabbit(s.width_of_images['rabbit'],
                                  s.width_of_images['rabbit'],
                                  'hp', dude, randint(0, 1) * 1400 - 100,
                                  388, 5 / g.FPS * 30, 15 / g.FPS * 30,
                                  3, 10, 1, 10, s.surface_of_rabbit_left
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
