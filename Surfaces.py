import pygame
from pygame import draw as draw
import Global_variable as G
from Functions import create_label

shop_button = create_label('shop', 60, 100, 50, False, True, G.GREEN)  # кнопка доступа к магазину

shop_window = pygame.Surface((1000, 500), pygame.SRCALPHA)
shop_window.fill(G.BLACK)
image_of_gun = pygame.Surface((250, 150), pygame.SRCALPHA)  # (вспомогательная штука; жду реальных озображений оружия)


surface_of_dude_left = pygame.Surface((24, 52), pygame.SRCALPHA) #поверхность, на которой нарисован человечек
surface_of_dude_left.fill(G.WHITE)
draw.polygon(surface_of_dude_left, G.BLACK, [(0, 0), (24, 0), (24, 40), (0, 40)])#контур
draw.polygon(surface_of_dude_left, (255, 187, 159), [(2, 2), (22, 2), (22, 20), (2, 20)])#лицо
draw.rect(surface_of_dude_left, (233, 150, 142), (2, 4, 16, 4))#лоб
draw.rect(surface_of_dude_left, (227, 126, 140), (2, 10, 16, 8))#щеки
draw.rect(surface_of_dude_left, (205, 111, 125), (2, 10, 12, 6))#под глазами
draw.rect(surface_of_dude_left, G.BLACK, (2, 10, 4, 4))#л глаз
draw.rect(surface_of_dude_left, G.BLACK, (10, 10, 4, 4))#пр глаз
draw.rect(surface_of_dude_left, (191, 84, 114), (2, 20, 20, 2))#подбородок
draw.rect(surface_of_dude_left, (176, 0, 7), (2, 22, 20, 16))#одежда
draw.rect(surface_of_dude_left, (147, 0, 55), (4, 26, 12, 12))#одежда тень
draw.rect(surface_of_dude_left, G.BLACK, (4, 40, 4, 12))#л нога
draw.rect(surface_of_dude_left, G.BLACK, (16, 40, 4, 12))#п нога
surface_of_dude_left.set_colorkey(G.WHITE)

surface_of_dude_right = pygame.Surface((24, 52), pygame.SRCALPHA)  # поверхность, на которой нарисован человечек
surface_of_dude_right.fill(G.WHITE)
draw.polygon(surface_of_dude_right, G.BLACK, [(0, 0), (24, 0), (24, 40), (0, 40)])#контур
draw.polygon(surface_of_dude_right, (255, 187, 159), [(2, 2), (22, 2), (22, 20), (2, 20)])#лицо
draw.rect(surface_of_dude_right, (233, 150, 142), (6, 4, 16, 4))#лоб
draw.rect(surface_of_dude_right, (227, 126, 140), (6, 10, 16, 8))#щеки
draw.rect(surface_of_dude_right, (205, 111, 125), (8, 10, 12, 6))#под глазами
draw.rect(surface_of_dude_right, G.BLACK, (10, 10, 4, 4))#л глаз
draw.rect(surface_of_dude_right, G.BLACK, (18, 10, 4, 4))#пр глаз
draw.rect(surface_of_dude_right, (191, 84, 114), (2, 20, 20, 2))#подбородок
draw.rect(surface_of_dude_right, (176, 0, 7), (2, 22, 20, 16))#одежда
draw.rect(surface_of_dude_right, (147, 0, 55), (8, 26, 12, 12))#одежда тень
draw.rect(surface_of_dude_right, G.BLACK, (4, 40, 4, 12))#л нога
draw.rect(surface_of_dude_right, G.BLACK, (16, 40, 4, 12))#п нога
surface_of_dude_right.set_colorkey(G.WHITE)

surface_of_zombie_right = pygame.Surface((24, 52), pygame.SRCALPHA) #поверхность, на которой надо бы нарисовать человечка, а не просто круг...
surface_of_zombie_right.fill(G.WHITE)
draw.polygon(surface_of_zombie_right, G.BLACK, [(0, 0), (24, 0), (24, 40), (0, 40)])#контур
draw.polygon(surface_of_zombie_right, (41, 207, 99), [(2, 2), (22, 2), (22, 20), (2, 20)])#лицо
draw.rect(surface_of_zombie_right, (61, 156, 201), (6, 4, 16, 4))#лоб
draw.rect(surface_of_zombie_right, (31, 128, 173), (6, 10, 16, 8))#щеки
draw.rect(surface_of_zombie_right, (31, 128, 173), (8, 10, 12, 6))#под глазами
draw.rect(surface_of_zombie_right, G.BLACK, (8, 12, 4, 4))#л глаз
draw.rect(surface_of_zombie_right, G.BLACK, (18, 12, 4, 4))#пр глаз
draw.rect(surface_of_zombie_right, (31, 128, 173), (2, 20, 20, 2))#подбородок
draw.rect(surface_of_zombie_right, (6, 90, 163), (2, 22, 20, 16))#одежда
draw.rect(surface_of_zombie_right, (37, 60, 190), (8, 26, 12, 12))#одежда тень
draw.rect(surface_of_zombie_right, G.BLACK, (4, 40, 4, 12))#л нога
draw.rect(surface_of_zombie_right, G.BLACK, (16, 40, 4, 12))#п нога
surface_of_zombie_right.set_colorkey(G.WHITE)

surface_of_zombie_left = pygame.Surface((24, 52), pygame.SRCALPHA) #поверхность, на которой надо бы нарисовать человечка, а не просто круг...
surface_of_zombie_left.fill(G.WHITE)
draw.polygon(surface_of_zombie_left, G.BLACK, [(0, 0), (24, 0), (24, 40), (0, 40)])#контур
draw.polygon(surface_of_zombie_left, (41, 207, 99), [(2, 2), (22, 2), (22, 20), (2, 20)])#лицо
draw.rect(surface_of_zombie_left, (61, 156, 201), (4, 4, 16, 4))#лоб
draw.rect(surface_of_zombie_left, (31, 128, 173), (4, 10, 16, 8))#щеки
draw.rect(surface_of_zombie_left, (31, 128, 173), (6, 10, 12, 6))#под глазами
draw.rect(surface_of_zombie_left, G.BLACK, (4, 12, 4, 4))#л глаз
draw.rect(surface_of_zombie_left, G.BLACK, (14, 12, 4, 4))#пр глаз
draw.rect(surface_of_zombie_left, (31, 128, 173), (2, 20, 20, 2))#подбородок
draw.rect(surface_of_zombie_left, (6, 90, 163), (2, 22, 20, 16))#одежда
draw.rect(surface_of_zombie_left, (37, 60, 190), (6, 26, 12, 12))#одежда тень
draw.rect(surface_of_zombie_left, G.BLACK, (4, 40, 4, 12))#л нога
draw.rect(surface_of_zombie_left, G.BLACK, (16, 40, 4, 12))#п нога
surface_of_zombie_left.set_colorkey(G.WHITE)

surface_of_rabbit_left = pygame.Surface((19, 15), pygame.SRCALPHA)
surface_of_rabbit_left.fill(G.WHITE)
draw.polygon(surface_of_rabbit_left, G.BLACK, [(0, 0), (10, 0), (10, 6), (18, 6), (18, 14), (0, 14)])
draw.polygon(surface_of_rabbit_left, (44, 232, 244), [(2, 6), (16, 8), (16, 12), (2, 12)])
draw.polygon(surface_of_rabbit_left, (60, 223, 196), [(2, 2), (4, 2), (4, 6), (6, 6), (6, 2), (8, 2), (8, 8), (2, 8)])
draw.polygon(surface_of_rabbit_left, G.BLACK, [(2, 8), (4, 8), (4, 10), (2, 10)])
draw.polygon(surface_of_rabbit_left, G.BLACK, [(6, 8), (8, 8), (8, 10), (6, 10)])
surface_of_rabbit_left.set_colorkey(G.WHITE)

surface_of_rabbit_right = pygame.transform.flip(surface_of_rabbit_left, 1, 0)
surface_of_rabbit_right.set_colorkey(G.WHITE)