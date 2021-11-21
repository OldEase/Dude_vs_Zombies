import pygame
from pygame import draw as draw
import Global_variable as G

surface_of_dude = pygame.Surface((200, 200), pygame.SRCALPHA)
draw.circle(surface_of_dude, G.RED, (100, 100), 30)