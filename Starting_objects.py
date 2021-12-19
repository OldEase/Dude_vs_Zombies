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

car = C.Car(500, 342, 0,
            0, False, 2000,
            S.surface_of_car,
            S.width_of_images['car'],
            S.height_of_images['car']
            )
dude = C.Dude(550, 350, 0,
              0, 10 / FPS * 30,
              8, 1, 0, 1000,
              [0] * 10, 2000, car,
              S.surface_of_dude_left, 'hp',
              S.width_of_images['dude'],
              S.height_of_images['dude'],
              {'fact': False, 'time': 0}
              )
button_shop = [C.ButtonObjects(1100, 0, S.shop_button),
               C.ButtonObjects(1100, 0, S.shop_close_button)]
start_button = C.ButtonObjects(400, 350, S.start_window)
quit_button = C.ButtonObjects(400, 340, S.quit_window)

full_arsenal = []

full_arsenal.append(Gn.Gun(S.surface_of_pistol,
                           speed=500, damage=2,
                           magaz=15, reload=2000,
                           amount=1, spread=2, long=45
                           )
                    )
full_arsenal.append(Gn.Gun(S.surface_of_revolver,
                           speed=1000, damage=5,
                           magaz=6, reload=3000,
                           amount=1, spread=1, long=45
                           )
                    )
full_arsenal.append(Gn.Gun(S.surface_of_shotgun,
                           speed=1000, damage=1,
                           magaz=2, reload=3000,
                           amount=10, spread=300, long=45
                           )
                    )
full_arsenal.append(Gn.Gun(S.surface_of_uzi,
                           speed=100, damage=1,
                           magaz=30, reload=3000,
                           amount=1, spread=5, long=45
                           )
                    )
full_arsenal.append(Gn.Gun(S.surface_of_rifle,
                           speed=1000, damage=5,
                           magaz=5, reload=3000,
                           amount=1, spread=2, long=45
                           )
                    )
