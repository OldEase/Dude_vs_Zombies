import pygame
from pygame import draw as draw
import Global_variable as G
from Functions import create_label

pygame.init()

width_of_images = {'dude': 24, 'zombie': 24, 'rabbit': 19, 'car': 100}
height_of_images = {'dude': 52, 'zombie': 52, 'rabbit': 15, 'car': 60}

shop_button = create_label('shop', 60, 100, 50, False, True, G.GREEN)  # кнопка доступа к магазину
shop_close_button = create_label('close', 60, 100, 50, False, True, G.GREEN)  # кнопка закрытия магазина

font_money = pygame.font.Font(None, 36)

shop_window = pygame.Surface((1000, 500), pygame.SRCALPHA)
shop_window.fill(G.BLACK)
image_of_gun = pygame.Surface((250, 150), pygame.SRCALPHA)  # (вспомогательная штука; жду реальных озображений оружия)

surface_of_car = pygame.Surface((width_of_images['car'], height_of_images['car']), pygame.SRCALPHA)
# поверхность, на которой нарисована машина
draw.rect(surface_of_car, G.BLACK,
          (0, 0, width_of_images['car'], height_of_images['car']))
draw.rect(surface_of_car, G.LIGHT_YELLOW,
          (2, 2, width_of_images['car'] - 4, height_of_images['car'] - 4))
draw.rect(surface_of_car, (0, 0, 100),
          (10, 10, 30, 30))
draw.rect(surface_of_car, (0, 0, 100),
          (60, 10, 30, 30))
draw.rect(surface_of_car, G.BLACK,
          (10, 45, 15, 15))
draw.rect(surface_of_car, G.BLACK,
          (75, 45, 15, 15))
draw.rect(surface_of_car, G.GRAY,
          (13, 48, 9, 9))
draw.rect(surface_of_car, G.GRAY,
          (78, 48, 9, 9))

surface_of_dude_left=pygame.Surface(
    (width_of_images['dude'], height_of_images['dude']), pygame.SRCALPHA)
# поверхность, на которой нарисован человечек
surface_of_dude_left.fill(G.WHITE)
draw.polygon(surface_of_dude_left, G.BLACK, [
             (0, 0), (24, 0), (24, 40), (0, 40)])  # контур
draw.polygon(surface_of_dude_left, (255, 187, 159), [
             (2, 2), (22, 2), (22, 20), (2, 20)])  # лицо
draw.rect(surface_of_dude_left, (233, 150, 142), (2, 4, 16, 4))  # лоб
draw.rect(surface_of_dude_left, (227, 126, 140), (2, 10, 16, 8))  # щеки
draw.rect(surface_of_dude_left, (205, 111, 125),
          (2, 10, 12, 6))  # под глазами
draw.rect(surface_of_dude_left, G.BLACK, (2, 10, 4, 4))  # л глаз
draw.rect(surface_of_dude_left, G.BLACK, (10, 10, 4, 4))  # пр глаз
draw.rect(surface_of_dude_left, (191, 84, 114), (2, 20, 20, 2))  # подбородок
draw.rect(surface_of_dude_left, (176, 0, 7), (2, 22, 20, 16))  # одежда
draw.rect(surface_of_dude_left, (147, 0, 55), (4, 26, 12, 12))  # одежда тень
draw.rect(surface_of_dude_left, G.BLACK, (4, 40, 4, 12))  # л нога
draw.rect(surface_of_dude_left, G.BLACK, (16, 40, 4, 12))  # п нога
surface_of_dude_left.set_colorkey(G.WHITE)

surface_of_dude_right=pygame.Surface(
    (width_of_images['dude'], height_of_images['dude']), pygame.SRCALPHA)  #
# поверхность, на которой нарисован человечек
surface_of_dude_right.fill(G.WHITE)
draw.polygon(surface_of_dude_right, G.BLACK, [
             (0, 0), (24, 0), (24, 40), (0, 40)])  # контур
draw.polygon(surface_of_dude_right, (255, 187, 159), [
             (2, 2), (22, 2), (22, 20), (2, 20)])  # лицо
draw.rect(surface_of_dude_right, (233, 150, 142), (6, 4, 16, 4))  # лоб
draw.rect(surface_of_dude_right, (227, 126, 140), (6, 10, 16, 8))  # щеки
draw.rect(surface_of_dude_right, (205, 111, 125),
          (8, 10, 12, 6))  # под глазами
draw.rect(surface_of_dude_right, G.BLACK, (10, 10, 4, 4))  # л глаз
draw.rect(surface_of_dude_right, G.BLACK, (18, 10, 4, 4))  # пр глаз
draw.rect(surface_of_dude_right, (191, 84, 114),
          (2, 20, 20, 2))  # подбородок
draw.rect(surface_of_dude_right, (176, 0, 7), (2, 22, 20, 16))  # одежда
draw.rect(surface_of_dude_right, (147, 0, 55),
          (8, 26, 12, 12))  # одежда тень
draw.rect(surface_of_dude_right, G.BLACK, (4, 40, 4, 12))  # л нога
draw.rect(surface_of_dude_right, G.BLACK, (16, 40, 4, 12))  # п нога
surface_of_dude_right.set_colorkey(G.WHITE)

surface_of_zombie_right=pygame.Surface(
    (width_of_images['zombie'], height_of_images['zombie']), pygame.SRCALPHA)
# поверхность, на которой надо бы нарисовать человечка, а не просто круг...
surface_of_zombie_right.fill(G.WHITE)
draw.polygon(surface_of_zombie_right, G.BLACK, [
             (0, 0), (24, 0), (24, 40), (0, 40)])  # контур
draw.polygon(surface_of_zombie_right, (41, 207, 99), [
             (2, 2), (22, 2), (22, 20), (2, 20)])  # лицо
draw.rect(surface_of_zombie_right, (61, 156, 201), (6, 4, 16, 4))  # лоб
draw.rect(surface_of_zombie_right, (31, 128, 173), (6, 10, 16, 8))  # щеки
draw.rect(surface_of_zombie_right, (31, 128, 173),
          (8, 10, 12, 6))  # под глазами
draw.rect(surface_of_zombie_right, G.BLACK, (8, 12, 4, 4))  # л глаз
draw.rect(surface_of_zombie_right, G.BLACK, (18, 12, 4, 4))  # пр глаз
draw.rect(surface_of_zombie_right, (31, 128, 173),
          (2, 20, 20, 2))  # подбородок
draw.rect(surface_of_zombie_right, (6, 90, 163), (2, 22, 20, 16))  # одежда
draw.rect(surface_of_zombie_right, (37, 60, 190),
          (8, 26, 12, 12))  # одежда тень
draw.rect(surface_of_zombie_right, G.BLACK, (4, 40, 4, 12))  # л нога
draw.rect(surface_of_zombie_right, G.BLACK, (16, 40, 4, 12))  # п нога
surface_of_zombie_right.set_colorkey(G.WHITE)

surface_of_zombie_left=pygame.Surface(
    (width_of_images['zombie'], height_of_images['zombie']), pygame.SRCALPHA)
surface_of_zombie_left.fill(G.WHITE)
draw.polygon(surface_of_zombie_left, G.BLACK, [
             (0, 0), (24, 0), (24, 40), (0, 40)])  # контур
draw.polygon(surface_of_zombie_left, (41, 207, 99), [
             (2, 2), (22, 2), (22, 20), (2, 20)])  # лицо
draw.rect(surface_of_zombie_left, (61, 156, 201), (4, 4, 16, 4))  # лоб
draw.rect(surface_of_zombie_left, (31, 128, 173), (4, 10, 16, 8))  # щеки
draw.rect(surface_of_zombie_left, (31, 128, 173),
          (6, 10, 12, 6))  # под глазами
draw.rect(surface_of_zombie_left, G.BLACK, (4, 12, 4, 4))  # л глаз
draw.rect(surface_of_zombie_left, G.BLACK, (14, 12, 4, 4))  # пр глаз
draw.rect(surface_of_zombie_left, (31, 128, 173),
          (2, 20, 20, 2))  # подбородок
draw.rect(surface_of_zombie_left, (6, 90, 163), (2, 22, 20, 16))  # одежда
draw.rect(surface_of_zombie_left, (37, 60, 190),
          (6, 26, 12, 12))  # одежда тень
draw.rect(surface_of_zombie_left, G.BLACK, (4, 40, 4, 12))  # л нога
draw.rect(surface_of_zombie_left, G.BLACK, (16, 40, 4, 12))  # п нога
surface_of_zombie_left.set_colorkey(G.WHITE)

surface_of_rabbit_left=pygame.Surface(
    (width_of_images['rabbit'], height_of_images['rabbit']), pygame.SRCALPHA)
surface_of_rabbit_left.fill(G.WHITE)
draw.polygon(surface_of_rabbit_left, G.BLACK, [
             (0, 0), (10, 0), (10, 6), (18, 6), (18, 14), (0, 14)])
draw.polygon(surface_of_rabbit_left, (44, 232, 244),
             [(2, 6), (16, 8), (16, 12), (2, 12)])
draw.polygon(surface_of_rabbit_left, (60, 223, 196), [
             (2, 2), (4, 2), (4, 6), (6, 6), (6, 2), (8, 2), (8, 8), (2, 8)])
draw.polygon(surface_of_rabbit_left, G.BLACK, [
             (2, 8), (4, 8), (4, 10), (2, 10)])
draw.polygon(surface_of_rabbit_left, G.BLACK, [
             (6, 8), (8, 8), (8, 10), (6, 10)])
surface_of_rabbit_left.set_colorkey(G.WHITE)

surface_of_rabbit_right=pygame.transform.flip(surface_of_rabbit_left, 1, 0)
surface_of_rabbit_right.set_colorkey(G.WHITE)

surface_of_pistol=pygame.Surface((75 + 25, 15), pygame.SRCALPHA)
surface_of_pistol.fill(G.WHITE)
surface_of_pistol.set_colorkey(G.WHITE)
draw.polygon(surface_of_pistol, G.BLACK, [
             (54 + 25, 0), (72 + 25, 0), (72 + 25, 6), (60 + 25, 6), (60 + 25, 12), (54 + 25, 12)])

surface_of_revolver=pygame.Surface((100, 15), pygame.SRCALPHA)
surface_of_revolver.fill(G.WHITE)
surface_of_revolver.set_colorkey(G.WHITE)
draw.polygon(surface_of_revolver, G.BLACK, [(79, 6), (82, 6), (82, 3), (96, 3), (96, 0), (99, 0),
                                            (99, 6), (93, 6), (93, 11), (84, 11), (84, 18), (79, 18)])

surface_of_shotgun=pygame.Surface((150, 50), pygame.SRCALPHA)
surface_of_shotgun.fill(G.WHITE)
draw.rect(surface_of_shotgun, G.GRAY, (75, 36, 45, 6))
draw.rect(surface_of_shotgun, G.BLACK, (75, 36, 45, 6), 2)
draw.rect(surface_of_shotgun, (173, 135, 98), (65, 38, 15, 7))
draw.rect(surface_of_shotgun, G.BLACK, (65, 38, 15, 7), 2)

surface_of_uzi=pygame.Surface((100, 20), pygame.SRCALPHA)
surface_of_uzi.fill(G.WHITE)
draw.polygon(surface_of_uzi, G.BLACK, ((75, 0), (78, 0), (78, 3), (85, 3), (87, 0), (89, 0), (89, 3),
             (94, 3), (94, 5), (99, 5), (99, 7), (94, 7), (94, 9), (83, 9), (85, 25), (80, 25), (80, 9), (75, 9)))

surface_of_rifle=pygame.Surface((150, 20 + 30), pygame.SRCALPHA)
surface_of_rifle.fill(G.WHITE)
draw.polygon(surface_of_rifle, G.BLACK, ((65, 7 + 30), (68, 7 + 30), (68, 3 + 30), (112, 3 + 30), (112, 0 + 30),
             (115, 0 + 30), (115, 3 + 30), (120, 3 + 30), (120, 8 + 30), (95, 8 + 30), (95, 11 + 30), (70, 11 + 30), (70, 15 + 30), (65, 15 + 30)))

health_empty=pygame.Surface((400, 10), pygame.SRCALPHA)
health_empty.fill((255, 255, 255))

surface_background=pygame.Surface((3600, 800), pygame.SRCALPHA)
surface_background.fill(G.BLACK)
for k in range(6):
    grass=[(0, 800)]
    for i in range(1000 - k * 150):
        grass.append((i * 3600 / (1000 - k * 150) + 1800
                     / (1000 - k * 150), 150 + k * 100))
        grass.append((i * 3600 / (1000 - k * 150) + 3600
                     / (1000 - k * 150), 140 + k * 100))
    grass.append((3600, 800))
    draw.polygon(surface_background, (5, 32 + k * 20, 53), grass)
