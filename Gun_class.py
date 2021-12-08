import math
from random import *
import pygame
import numpy as np
import Surfaces as S
import Global_variable as G

sr = pygame.Surface((180, 80))


class gun():
    def __init__(self, image):
        self.x = 130
        self.y = 35
        self.speed = 10
        self.damage = 1
        self.magaz = 10
        self.reload = 5
        self.amount = 1
        self.spread = 10
        self.image = image

    def draw(self):
        pygame.draw.rect(sr, G.BLUE, (self.x, self.y, 50, 10))
        pygame.draw.rect(sr, G.BLUE, (self.x, self.y + 10, 10, 15))

    def shot(self, dude, pos):
        G.bullets.append(bullet(pos, (dude.x + 12, dude.y + 24), self))
        

def muv(sr, pos, coord):
    x1, y1 = pos[0], pos[1]
    x, y = coord[0], coord[1]
    angle = np.arctan2((x1 - x), (y1 - y)) * 180 / np.pi
    sr1 = pygame.transform.rotate(sr, angle - 90)
    return sr1, sr1.get_size(), angle

class bullet:
    def __init__(self, pos, coord, gun):
        h = 8
        R = ((coord[0] - pos[0])**2 + (coord[1] - pos[1])**2)**0.5
        self.x = coord[0] + h * -(coord[0] - pos[0]) / R
        self.y = coord[1] + h * -(coord[1] - pos[1]) / R
        self.h = 60
        self.x1 = coord[0] + h * - \
            (coord[0] - pos[0]) / R - (coord[0] - pos[0]) / self.h
        self.y1 = coord[1] + h * - \
            (coord[1] - pos[1]) / R - (coord[1] - pos[1]) / self.h
        screed = pygame.Surface((10, 10))
        pygame.draw.polygon(screed, G.GRAY, ((self.x, self.y - 1), (self.x1, self.y1 - 1),
                (self.x1, self.y1 + 1), (self.x, self.y + 1)), 0)
        self.angle = 3 * randint(-gun.spread, gun.spread) / 100

        self.check = True

        self.V = 10
        self.dx = self.V * -(coord[0] - pos[0]) / R
        self.dy = self.V * -(coord[1] - pos[1]) / R + self.angle
        self.image = screed

    def dvizh(self, coord_kako):

        self.x += self.dx
        self.y += self.dy
        self.x1 += self.dx
        self.y1 += self.dy
        pygame.draw.polygon(screen, G.GREY, ((self.x, self.y - 1), (self.x1, self.y1 - 1),
                (self.x1, self.y1 + 1), (self.x, self.y + 1)), 0)


pygame.display.update()
clock = pygame.time.Clock()
finished=False

Gun = gun(S.surface_of_pistol)
Gun.draw()
coord = [200, 405]
ch=False