import pygame
import surfaces as s
import classes as c
import functions as f
import global_variable as g
import special_functions
import starting_objects as obj
import motion_objects as motion
import gun_class as gn
from random import *

pygame.init()

pygame.mixer.music.load('ost.mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play()

full_arsenal = obj.full_arsenal
arsenal = [full_arsenal[0]] * 5
car, dude, button_shop, start_button, quit_button, zombies = obj.car, obj.dude, obj.button_shop, \
    obj.start_button, obj.quit_button, []
objects = {'car': car,
           'dude': dude,
           'button_shop': button_shop,
           'zombies': [],
           'rabbit': []
           }

shop = special_functions.create_shop(dude)
gun = arsenal[0]
coord = [560, 370]

pygame.display.update()
clock = pygame.time.Clock()
result = 'ПОРАЖЕНИЕ'
time = 0
background = c.Background(s.surface_background)
side_gun_check = "right"
health = c.Health(s.health_empty)
spawn_time = 0
spawn_check = False
spawn_counter = 0
spawn_dif = 3
spawn_cooldown = 0
Mask_dude = pygame.mask.from_surface(dude.image)

start = False  # логическая переменная, отвечающая за начало игры
finished = False  # логическая переменная, отвечающая за окончание игры
quit = False

while (not start) and (not finished):  # цикл, который выводит начальную заставку, пока игрок не нажмет "start"
    clock.tick(g.FPS)
    events = pygame.event.get()
    for event in events:
        start, finished, quit = f.start_game(event,
                                             start_button,
                                             start, finished,
                                             quit
                                             )
    g.screen.fill(g.BLACK)
    g.screen.blit(s.text_title, (200, 200))
    f.draw_object(start_button)
    pygame.display.update()

while not finished:  # основной цикл программы
    clock.tick(g.FPS)
    events = pygame.event.get()
    pos = pygame.mouse.get_pos()

    objects['zombies'], spawn_time, spawn_check, spawn_counter, spawn_dif, spawn_cooldown = \
        special_functions.spawn_checking(objects['zombies'],
                                         dude, spawn_time,
                                         spawn_check, spawn_counter,
                                         spawn_dif, spawn_cooldown,
                                         time
                                         )

    objects, g.bullets = motion.motion_objects(objects, background,
                                               gun, g.bullets, shop['open'],
                                               health, pos, time
                                               )
    car, dude, zombies = objects['car'], objects['dude'], objects['zombies']
    f.draw_object(dude.car)
    f.draw_object(dude)

    text_money = s.font_money.render('$ ' + str(dude.money), True, g.WHITE)
    text_xp = s.font_money.render(
        'XP ' + str(dude.xp) + '/' + str(dude.lvl_up), True, g.WHITE)
    text_medkit = s.font_money.render(
        'Medkit ' + str(dude.medkit), True, g.WHITE)
    text_gun = s.font_money.render(str(gun.load) + '/' + str(gun.magaz), True, g.WHITE)
    g.screen.blit(text_money, (50, 50))
    g.screen.blit(text_gun, (50, 110))
    g.screen.blit(text_xp, (50, 20))
    g.screen.blit(text_medkit, (50, 80))
    sr1, coord_change, angel = gn.muv(gun.image, pos, coord)

    dude, background = f.checking_of_stun(dude, background)

    for event in events:  # блок обработки выполненных игроком действий
        shop['open'], finished, quit = f.handle_events(event, shop['open'],
                                                       finished, quit
                                                       )
    dude.handle_pressing_keys(shop['open'], time, g.g / g.FPS * 30)

    if f.check(pygame.key.get_pressed()[pygame.K_1],
               pygame.key.get_pressed()[pygame.K_2],
               pygame.key.get_pressed()[pygame.K_3],
               pygame.key.get_pressed()[pygame.K_4],
               pygame.key.get_pressed()[pygame.K_5]
               ):
        gun = arsenal[f.choose(pygame.key.get_pressed()[pygame.K_1],
                               pygame.key.get_pressed()[pygame.K_2],
                               pygame.key.get_pressed()[pygame.K_3],
                               pygame.key.get_pressed()[pygame.K_4],
                               pygame.key.get_pressed()[pygame.K_5]
                               )
        ]

    sr1.set_colorkey(g.WHITE)
    g.screen.blit(sr1, (dude.x + 10 - coord_change[0] / 2, dude.y + 10 - coord_change[1] / 2))
    if dude.x < pos[0] and side_gun_check == "left":
        dude.image = s.surface_of_dude_right
        gun.image = gun.image_right
        side_gun_check = "right"

    if dude.x > pos[0] and side_gun_check == "right":
        dude.image = s.surface_of_dude_left
        gun.image = gun.image_left
        side_gun_check = "left"

    live_objects = f.update_live_objects(objects)
    for object in live_objects:
        f.draw_hp(object)
    f.draw_rapair_level(car)

    if shop['open']:
        g.screen.blit(shop['image'].image, (shop['image'].x, shop['image'].y))
        for event in events:  # блок обработки выполненных игроком в магазине действий
            dude, arsenal = f.shop_actions(event, shop, dude, arsenal, full_arsenal)
        shop = special_functions.update_shop(shop, dude)
        f.draw_object(button_shop[1])
    else:
        f.draw_object(button_shop[0])

    result, finished = f.checking_of_end(dude.lives,
                                         dude.car.repair_level,
                                         dude.car.full_repair_level,
                                         result, finished
                                         )

    pygame.display.update()
    g.screen.fill(g.BLACK)

time = 0
result = f.create_label(result, 150, 800, 90, False, True, g.WHITE)

while (not quit) and (time <= 700):  # цикл, который выводит результат игры по ее окончании
    clock.tick(g.FPS)
    events = pygame.event.get()
    for event in events:
        quit = f.finish_game(event, quit_button, quit)
    g.screen.fill(g.BLACK)
    g.screen.blit(result, (250, 200))
    f.draw_object(quit_button)
    pygame.display.update()

pygame.quit()
