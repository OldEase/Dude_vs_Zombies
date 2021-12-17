import pygame
import numpy as np
import Surfaces as S
import Classes as C
import Functions as F
import Global_variable as G
import Zombies_class as Z
import Starting_functions
import Starting_objects as Obg
import Gun_class as Gn
from random import *

pygame.init()
FPS = 144  # число кадров в секунду

def motion_objects(objects, background, gun, bullets, time, health, pos):
    objects['dude'].check_collision_with_car()
    objects['dude'] = F.move_object(objects['dude'], objects['dude'])
    objects['dude'].car = F.move_object(objects['car'], objects['dude'])
    background = F.move_object(background, objects['dude'])
    F.draw_object(background)
    F.draw_object(health)
    F.draw_object(C.Health_full(objects['dude']))
    if not objects['dude'].stun['fact']:
        gun.shot(objects['dude'], pos, pygame.mouse.get_pressed()[0])

    objects['zombies'], objects['dude'], G.bullets = F.collision_with_zombie(objects['zombies'], objects['dude'],
                                                                                     bullets)

    for zombie in objects['zombies']:
        zombie.follow(objects['dude'])
        zombie, objects['dude'] = F.motion_processing(zombie, objects['dude'])
        F.draw_object(zombie)
    objects['rabbit'].follow(objects['dude'])
    objects['rabbit'], objects['dude'] = F.motion_processing(objects['rabbit'], objects['dude'])

    return objects, bullets


