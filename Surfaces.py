import pygame
from pygame import draw as draw
import Global_variable as G

surface_of_dude_left = pygame.Surface((24, 52), pygame.SRCALPHA) #поверхность, на которой надо бы нарисовать человечка, а не просто круг...
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

surface_of_dude_right = pygame.Surface((24, 52), pygame.SRCALPHA) #поверхность, на которой надо бы нарисовать человечка, а не просто круг...
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

surface_of_zombie = pygame.Surface((100, 100), pygame.SRCALPHA)
draw.polygon(surface_of_zombie, G.BLUE, [(8, 22), (32, 22), (32, 28), (30, 28), (30, 40), (22, 40), (22, 28), (18, 28), \
                                       (18, 40), (10, 40), (10, 28), (8, 28)])
draw.polygon(surface_of_zombie, G.RED, [(6, 10), (34, 10), (34, 22), (6, 22), (6, 16), (4, 16), (4, 20), (0, 20), \
                                       (0, 12), (6, 12)])
draw.rect(surface_of_zombie, G.GRAY, (12, 2, 16, 8))
draw.rect(surface_of_zombie, G.BLUE, (14, 4, 4, 2))
draw.rect(surface_of_zombie, G.BLUE, (22, 4, 4, 2))#

