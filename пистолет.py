import math
from random import *
import pygame
from pygame.draw import *
import numpy as np

FPS = 30
screen = pygame.display.set_mode((600, 600))
sr = pygame.Surface((180, 80))
angle0 = 0

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 1)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class gun():
    def __init__(self, sr):
        self.x = 90
        self.y = 35
        '''self.l = 50
        self.h = 10
        self.xl = 100
        self.yl = 0
        self.xw = self.yl / 10
        self.yw = self.xl / 10'''
        self.color = BLACK

    def draw(self):
        rect(sr, RED, (self.x, self.y, 50, 10))
        rect(sr, self.color, (self.x + 40, self.y - 15, 10, 15))
        rect(sr, self.color, (self.x + 40, self.y - 25, 50, 10))

def muv(sr, pos, coord):
    x1, y1 = pos[0], pos[1]
    x, y = coord[0] + 90, coord[1] + 40
    angle = np.arctan2((x1 - x), (y1 - y)) * 180 / np.pi
    sr1 = pygame.transform.rotate(sr, angle-90)
    return sr1
    








pygame.display.update()
clock=pygame.time.Clock()
finished=False

Gun=gun(sr)
Gun.draw()
coord = [200, 405]
ch=False

while not finished:
    clock.tick(FPS)
    screen.fill(WHITE)
    sr.set_colorkey((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pos = pygame.mouse.get_pos()
    sr1 = muv(sr, pos, coord)

    screen.blit(sr1, coord)
    pygame.display.update()
pygame.quit()