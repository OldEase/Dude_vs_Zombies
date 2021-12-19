import pygame
import classes as c
import functions as f
import global_variable as g

pygame.init()


def motion_objects(objects, background,
                   gun, bullets, shop_open,
                   health, pos, time
                   ):
    """
    Функция перемещающая все объекты
    """
    objects['dude'].check_collision_with_car()
    objects['dude'], background = limiting_of_space(objects['dude'], background)
    objects['dude'] = f.move_object(objects['dude'], objects['dude'])
    objects['dude'].car = f.move_object(objects['car'], objects['dude'])
    background = f.move_object(background, objects['dude'])
    f.draw_object(background)
    f.draw_object(health)
    if (not objects['dude'].stun['fact']) or (time % 40 >= 20):

        f.draw_object(c.HealthFull(objects['dude']))
    if (not objects['dude'].stun['fact']) and (not objects['dude'].car.repairing) \
            and (not shop_open) and len(objects['zombies']) != 0:
        gun.shot(objects['dude'], pos, pygame.mouse.get_pressed()[0])

    objects['zombies'], objects['dude'], g.bullets = f.collision_with_zombie(objects['zombies'],
                                                                             objects['dude'],
                                                                             bullets)

    for zombie in objects['zombies']:
        zombie.follow(objects['dude'])
        zombie.jump(objects['dude'])
        zombie, objects['dude'] = f.motion_processing(zombie, objects['dude'])
        f.draw_object(zombie)
    return objects, bullets


def limiting_of_space(dude, background
                      ):
    """
    следит за тем, чтобы герой не выбежал за пределы экрана
    """
    if background.x - dude.dx <= - 2400 + dude.width:
        dude.dx = background.x + 2400 - dude.width
    if background.x - dude.dx >= 0:
        dude.dx = background.x - 0
    return dude, background
