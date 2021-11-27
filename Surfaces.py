import pygame
from pygame import draw as draw
import Global_variable as G

surface_of_dude = pygame.Surface((100, 100), pygame.SRCALPHA) #поверхность, на которой надо бы нарисовать человечка, а не просто круг...
draw.polygon(surface_of_dude, G.BLUE, [(20, 55), (80, 55), (80, 70), (75, 70), (75, 100), (55, 100), (55, 70), (45, 70), \
                                       (45, 100), (25, 100), (25, 70), (20, 70)])
draw.polygon(surface_of_dude, G.RED, [(15, 25), (85, 25), (85, 55), (15, 55), (15, 40), (10, 40), (10, 50), (0, 50), \
                                       (0, 30), (15, 30)])
draw.rect(surface_of_dude, G.LIGHT_YELLOW, (30, 5, 40, 20))
draw.rect(surface_of_dude, G.BLUE, (35, 10, 10, 5))
draw.rect(surface_of_dude, G.BLUE, (55, 10, 10, 5))#

surface_of_zombie = pygame.Surface((100, 100), pygame.SRCALPHA)
draw.polygon(surface_of_zombie, G.BLUE, [(20, 55), (80, 55), (80, 70), (75, 70), (75, 100), (55, 100), (55, 70), (45, 70), \
                                       (45, 100), (25, 100), (25, 70), (20, 70)])
draw.polygon(surface_of_zombie, G.RED, [(15, 25), (85, 25), (85, 55), (15, 55), (15, 40), (10, 40), (10, 50), (0, 50), \
                                       (0, 30), (15, 30)])
draw.rect(surface_of_zombie, G.GRAY, (30, 5, 40, 20))
draw.rect(surface_of_zombie, G.BLUE, (35, 10, 10, 5))
draw.rect(surface_of_zombie, G.BLUE, (55, 10, 10, 5))#

