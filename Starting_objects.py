import pygame
import numpy as np
import Surfaces as S
import Classes as C
import Functions as F
import Global_variable as G
import Zombies_class as Z
import Special_functions
import Gun_class as Gn

FPS = 144

car = C.Car(500, 342, 0, 0, False, 2000, S.surface_of_car, S.width_of_images['car'], S.height_of_images['car'])
dude = C.Dude(550, 350, 0, 0, 10 / FPS * 30, 8, 1, 0, 100, [0] * 10, 20000, car, S.surface_of_dude_left, 'hp',
            S.width_of_images['dude'], S.height_of_images['dude'], {'fact':False, 'time': 0})
button_shop = [C.Button_objects(1100, 0, S.shop_button), C.Button_objects(1100, 0, S.shop_close_button)]
zombie1 = Z.Zombie(S.width_of_images['zombie'], S.width_of_images['zombie'], 'hp', dude, 50, 350, 3 / FPS * 30,
            10, 10, 10, 1, 1, S.surface_of_zombie_right)
zombie2 = Z.Zombie(S.width_of_images['zombie'], S.width_of_images['zombie'], 'hp', dude, 250, 350, 3 / FPS * 30,
            20, 10, 10, 1, 1, S.surface_of_zombie_right)
zombie3 = Z.Zombie(S.width_of_images['zombie'], S.width_of_images['zombie'],'hp', dude, 800, 350, 3 / FPS * 30,
            75, 10, 10, 1, 1, S.surface_of_zombie_right)
rabbit = Z.Rabbit(S.width_of_images['rabbit'], S.width_of_images['rabbit'], 'hp', 200, 388, 5 / FPS * 30, 10, 100,
            10, 1, 1, S.surface_of_rabbit_left)

full_arsenal = []
full_arsenal.append(Gn.gun(S.surface_of_pistol, speed=500, damage=2,
             magaz=15, reload=5000, amount=1, spread=2, long=45))
full_arsenal.append(Gn.gun(S.surface_of_revolver, speed=1000, damage=5,
             magaz=6, reload=7000, amount=1, spread=1, long=45))
full_arsenal.append(Gn.gun(S.surface_of_shotgun, speed=1000, damage=1,
             magaz=2, reload=5000, amount=10, spread=200, long=45))
full_arsenal.append(Gn.gun(S.surface_of_uzi, speed=100, damage=1,
             magaz=1000, reload=5000, amount=1, spread=1, long=45))
full_arsenal.append(Gn.gun(S.surface_of_rifle, speed=1000, damage=4,
             magaz=1000, reload=5000, amount=1, spread=1, long=45))
