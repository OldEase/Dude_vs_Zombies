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

pygame.init()
FPS = 144  # число кадров в секунду

pygame.mixer.music.load('ost.mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play()

arsenal = []
arsenal.append(Gn.gun(S.surface_of_pistol, speed=500, damage=2,
             magaz=15, reload=5000, amount=1, spread=2, long=45))
arsenal.append(Gn.gun(S.surface_of_revolver, speed=1000, damage=5,
             magaz=6, reload=7000, amount=1, spread=1, long=45))
arsenal.append(Gn.gun(S.surface_of_shotgun, speed=1000, damage=1,
             magaz=2, reload=5000, amount=10, spread=200, long=45))
arsenal.append(Gn.gun(S.surface_of_uzi, speed=100, damage=1,
             magaz=1000, reload=5000, amount=1, spread=1, long=45))
arsenal.append(Gn.gun(S.surface_of_rifle, speed=1000, damage=4,
             magaz=1000, reload=5000, amount=1, spread=1, long=45))
arsenal.append(Gn.gun(S.surface_of_shotgun, speed=100, damage=1,
             magaz=1000, reload=5000, amount=1, spread=1, long=45))
arsenal.append(Gn.gun(S.surface_of_shotgun, speed=100, damage=1,
             magaz=1000, reload=5000, amount=1, spread=1, long=45))
arsenal.append(Gn.gun(S.surface_of_shotgun, speed=100, damage=1,
             magaz=1000, reload=5000, amount=1, spread=1, long=45))
arsenal.append(Gn.gun(S.surface_of_shotgun, speed=100, damage=1,
             magaz=1000, reload=5000, amount=1, spread=1, long=45))

car, dude, button_shop, zombie1, zombie2, zombie3, rabbit = Obg.car, Obg.dude, Obg.button_shop, Obg.zombie1, \
    Obg.zombie2, Obg.zombie3, Obg.rabbit

zombies = [zombie1, zombie2, zombie3]
rabbits = [rabbit]
monsters = [zombies] + [rabbits]
shop = Starting_functions.create_shop()
gun = arsenal[0]
coord = [560, 370]
pygame.display.update()
clock = pygame.time.Clock()
finished = False
result = 'ПОРАЖЕНИЕ'
time = 0
background = C.Background(S.surface_background)
side_gun_check = "right"

Mask_dude = pygame.mask.from_surface(dude.image)

while (not finished) and (time < 100000):  # основной цикл программы
    clock.tick(FPS)
    '''if(Mask_dude.overlap_area(Mask_zombie, (int(zombie.x - dude.x), int(zombie.y - dude.y)))) != 0:
		print((int(zombie.x - dude.x), int(zombie.y - dude.y)))'''
    # zombie.image.fill(G.BLACK)
    events = pygame.event.get()
    G.screen.fill(G.LIGHT_YELLOW)
    dude.check_collision_with_car()
    dude = F.move_object(dude, dude)
    dude.car = F.move_object(car, dude)
    background = F.move_object(background, dude)
    F.draw_object(background)
    k = 0
    for zombie in zombies:
        if (dude.x - zombie.width <= zombie.x <= dude.x + dude.width) and (dude.y > zombie.y - dude.height) and      \
                not dude.stun['fact']:
            dude.lives += - zombie.damage
            if dude.x - zombie.x == 0:
                dude.dx = dude.width * 2
            else:
                dude.dx = (dude.x - zombie.x) / np.abs(dude.x - zombie.x) * 2 * dude.width
            dude.dy = 0
            dude.stun['fact'] = True
        counter = 0
        for bull in G.bullets:
            inside_check = False

            for i in range(bull.V):
                bull = F.move_bullet(bull)
                if (zombie.mask.overlap_area(bull.mask,
                        (int(-zombie.x + bull.x), int(-zombie.y + bull.y)))) != 0 and not inside_check:
                    (x, y) = zombie.mask.overlap(
                        bull.mask, (int(-zombie.x + bull.x), int(-zombie.y + bull.y)))
                    pygame.draw.rect(zombie.image, G.WHITE, (x, y, 2, 2))
                    pygame.draw.rect(zombie.image, G.RED, (x + 2 * bull.dx/abs(bull.dx), y, 1, 1))
                    zombie.mask = pygame.mask.from_surface(zombie.image)
                    zombie.lives += - bull.damage
                    print(bull.damage)
                    if zombie.lives <=0:
                        zombies.pop(k)
                    inside_check = True
                    G.bullets.pop(counter)
            if not inside_check:
                F.draw_object(bull)
            counter += 1
        k += 1

    for zombie in zombies:
        zombie.follow(dude)
        zombie, dude = F.motion_processing(zombie, dude)
        F.draw_object(zombie)
    rabbit.follow(dude)
    rabbit, dude = F.motion_processing(rabbit, dude)
    F.draw_object(dude.car)
    F.draw_object(dude)

    F.draw_object(rabbit)
    pos = pygame.mouse.get_pos()
    sr1, coord_change, angel = Gn.muv(gun.image, pos, coord)

    if dude.stun['fact']:
        if dude.stun['time'] > 0:
            dude.dx = 0
        dude.stun['time'] += 1
        if dude.stun['time'] >= 72:
            dude.stun['fact'], dude.stun['time'] = False, 0

    for event in events:  # блок обработки выполненных игроком действий
        shop['open'], finished = F.handle_events(event, shop['open'], finished)
    # if (event.type == pygame.MOUSEBUTTONDOWN) and (not shop['open']):
    # gun.shot(dude, pos, True, False)
    dude.handle_pressing_keys(shop['open'], time, G.g / FPS * 30)
    if not dude.stun['fact']:
        gun.shot(dude, pos, pygame.mouse.get_pressed()[0])
    if F.check(pygame.key.get_pressed()[
            pygame.K_1], pygame.key.get_pressed()[pygame.K_2], pygame.key.get_pressed()[pygame.K_3], pygame.key.get_pressed()[pygame.K_4], pygame.key.get_pressed()[pygame.K_5], pygame.key.get_pressed()[pygame.K_6], pygame.key.get_pressed()[pygame.K_7], pygame.key.get_pressed()[pygame.K_8], pygame.key.get_pressed()[pygame.K_9]):
        gun = arsenal[F.choose(pygame.key.get_pressed()[
            pygame.K_1], pygame.key.get_pressed()[pygame.K_2], pygame.key.get_pressed()[pygame.K_3], pygame.key.get_pressed()[pygame.K_4], pygame.key.get_pressed()[pygame.K_5], pygame.key.get_pressed()[pygame.K_6], pygame.key.get_pressed()[pygame.K_7], pygame.key.get_pressed()[pygame.K_8], pygame.key.get_pressed()[pygame.K_9])]

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
            C.Dude = F.shop_actions(event, shop, C.Dude)
        F.draw_object(button_shop[1])
    else:
        F.draw_object(button_shop[0])

    result, finished = F.checking_of_end(dude.lives, dude.car.repair_level, result, finished)
    time += 1
    pygame.display.update()
    G.screen.fill(G.BLACK)
print(result)
pygame.quit()
