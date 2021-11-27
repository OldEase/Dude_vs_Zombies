import pygame
from pygame import draw as draw
import Global_variable as G

surface_of_dude = pygame.Surface((40, 40), pygame.SRCALPHA) #поверхность, на которой надо бы нарисовать человечка, а не просто круг...
draw.polygon(surface_of_dude, G.BLUE, [(8, 22), (32, 22), (32, 28), (30, 28), (30, 40), (22, 40), (22, 28), (18, 28), \
                                       (18, 40), (10, 40), (10, 28), (8, 28)])
draw.polygon(surface_of_dude, G.RED, [(6, 10), (34, 10), (34, 22), (6, 22), (6, 16), (4, 16), (4, 20), (0, 20), \
                                       (0, 12), (6, 12)])
draw.rect(surface_of_dude, G.LIGHT_YELLOW, (12, 2, 16, 8))
draw.rect(surface_of_dude, G.BLUE, (14, 4, 4, 2))
draw.rect(surface_of_dude, G.BLUE, (22, 4, 4, 2))#

surface_of_zombie = pygame.Surface((100, 100), pygame.SRCALPHA)
draw.polygon(surface_of_zombie, G.BLUE, [(8, 22), (32, 22), (32, 28), (30, 28), (30, 40), (22, 40), (22, 28), (18, 28), \
                                       (18, 40), (10, 40), (10, 28), (8, 28)])
draw.polygon(surface_of_zombie, G.RED, [(6, 10), (34, 10), (34, 22), (6, 22), (6, 16), (4, 16), (4, 20), (0, 20), \
                                       (0, 12), (6, 12)])
draw.rect(surface_of_zombie, G.GRAY, (12, 2, 16, 8))
draw.rect(surface_of_zombie, G.BLUE, (14, 4, 4, 2))
draw.rect(surface_of_zombie, G.BLUE, (22, 4, 4, 2))#

