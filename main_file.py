import pygame
import numpy as np
import Surfaces as S
import Classes as C
import Functions as F
import Global_variable as G
import Zombies_class as Z
import Special_functions
import Starting_objects as Obg
import Motion_objects as Motion
import Gun_class as Gn
from random import *

pygame.init()
FPS = 144  # число кадров в секунду

pygame.mixer.music.load('ost.mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play()

full_arsenal = Obg.full_arsenal
arsenal = [full_arsenal[0]] * 5
car, dude, button_shop, zombies, rabbit = Obg.car, Obg.dude, Obg.button_shop, [Obg.zombie1, \
    Obg.zombie2, Obg.zombie3], Obg.rabbit
objects = {'car': car, 'dude': dude, 'button_shop': button_shop, 'zombies': [zombies[0], zombies[1],
            zombies[2]], 'rabbit': rabbit}
live_objects = {'dude': dude, 'zombie1': zombies[0], 'zombie2': zombies[1],
           'zombie3': zombies[2], 'rabbit': rabbit}
rabbits = [rabbit]
shop = Special_functions.create_shop()
gun = arsenal[0]
coord = [560, 370]
pygame.display.update()
clock = pygame.time.Clock()
finished = False
result = 'ПОРАЖЕНИЕ'
time = 0
background = C.Background(S.surface_background)
side_gun_check = "right"
health = C.Health(S.health_empty)
spawn_time = 0
spawn_check = False
spawn_counter = 0
spawn_dif = 3
spawn_cooldown = 0
Mask_dude = pygame.mask.from_surface(dude.image)

print(shop['guns'])
while (not finished):
    clock.tick(FPS)
    events = pygame.event.get()
    pos = pygame.mouse.get_pos()
    G.screen.fill(G.BLACK) 
    G.screen.blit(S.text_title, (200, 200))
    if pygame.time.get_ticks() > 5000:
        finished = True
    pygame.display.update()

finished = False

while (not finished):  # основной цикл программы
    clock.tick(FPS)
    events = pygame.event.get()
    pos = pygame.mouse.get_pos()
    objects, G.bullets = Motion.motion_objects(objects, background, gun, G.bullets, shop['open'], health, pos)
    car, dude, zombies, rabbit = objects['car'], objects['dude'], objects['zombies'], objects['rabbit']
    F.draw_object(dude.car)
    F.draw_object(dude)

    F.draw_object(rabbit)
    text_money = S.font_money.render('$ ' + str(dude.money), True, G.WHITE)
    text_xp = S.font_money.render(
        'XP ' + str(dude.xp) + '/' + str(dude.lvl_up), True, G.WHITE)
    text_medkit = S.font_money.render(
        'Medkit ' + str(dude.medkit), True, G.WHITE)
    text_gun = S.font_money.render(str(gun.load) + '/' + str(gun.magaz), True, G.WHITE)
    G.screen.blit(text_money, (50, 50))
    G.screen.blit(text_gun, (50, 110))
    G.screen.blit(text_xp, (50, 20))
    G.screen.blit(text_medkit, (50, 80))
    sr1, coord_change, angel = Gn.muv(gun.image, pos, coord)

    dude, background = F.checking_of_stun(dude, background)

    for event in events:  # блок обработки выполненных игроком действий
        shop['open'], finished = F.handle_events(
            event, shop['open'], finished)
    dude.handle_pressing_keys(shop['open'], time, G.g / FPS * 30)

    if pygame.key.get_pressed()[pygame.K_RCTRL]:
        gun.reload()
    
    if F.check(pygame.key.get_pressed()[
            pygame.K_1], pygame.key.get_pressed()[pygame.K_2], pygame.key.get_pressed()[pygame.K_3], pygame.key.get_pressed()[pygame.K_4], pygame.key.get_pressed()[pygame.K_5]):
        gun = arsenal[F.choose(pygame.key.get_pressed()[
            pygame.K_1], pygame.key.get_pressed()[pygame.K_2], pygame.key.get_pressed()[pygame.K_3], pygame.key.get_pressed()[pygame.K_4], pygame.key.get_pressed()[pygame.K_5])]

    sr1.set_colorkey(G.WHITE)
    G.screen.blit(sr1, (dude.x + 10 - coord_change[0] / 2, dude.y + 10 - coord_change[1] / 2))
    if dude.x < pos[0] and side_gun_check == "left":
        dude.image = S.surface_of_dude_right
        gun.image = gun.image_right
        side_gun_check = "right"

    if dude.x > pos[0] and side_gun_check == "right":
        dude.image = S.surface_of_dude_left
        gun.image = gun.image_left
        side_gun_check = "left"
    if shop['open']:
        G.screen.blit(shop['image'].image, (shop['image'].x, shop['image'].y))
        for event in events:  # блок обработки выполненных игроком в магазине действий
            dude, arsenal = F.shop_actions(event, shop, dude, arsenal, full_arsenal)
        F.draw_object(button_shop[1])
    else:
        F.draw_object(button_shop[0])

    result, finished = F.checking_of_end(dude.lives, dude.car.repair_level, dude.car.full_repair_level, result,
                                                                                                        finished)

    objects['zombies'], spawn_time, spawn_check, spawn_counter, spawn_dif, spawn_cooldown = Special_functions.spaun_checking(objects['zombies'],
            dude, spawn_time, spawn_check, spawn_counter, spawn_dif, spawn_cooldown)

    live_objects = F.update_live_objects(objects)

    for object in live_objects:
        F.draw_hp(object)
    F.draw_rapair_level(car)
    pygame.display.update()
    G.screen.fill(G.BLACK)
print(result)
pygame.quit()
