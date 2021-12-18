import math
from random import *
import pygame
import numpy as np
import Surfaces as S
import Global_variable as G

sr = pygame.Surface((180, 80))

class gun():
    def __init__(self, image, speed=1000, damage=1, magaz=10, reload=5000, amount=5, spread=10,
                 long=45):
        self.x = 130
        self.y = 35
        self.h = long
        self.speed = speed
        self.shot_time = 0
        self.damage = damage
        self.magaz = magaz
        self.load = self.magaz
        self.reload = reload
        self.load_time = 0
        self.amount = amount
        self.spread = spread
        self.image = image
        self.image_right = image
        self.image_left = pygame.transform.flip(image, 0, 1)

    def draw(self):
        pygame.draw.rect(sr, G.BLUE, (self.x, self.y, 50, 10))
        pygame.draw.rect(sr, G.BLUE, (self.x, self.y + 10, 10, 15))

    def shot(self, dude, pos, check):
        if self.load == 0 and self.load_time + self.reload < pygame.time.get_ticks() and check:
            self.load = self.magaz
        if self.load != 0 and self.shot_time + self.speed < pygame.time.get_ticks() and check:
            for i in range(self.amount):
                G.bullets.append(
                    bullet(pos, (dude.x + 8, dude.y), self))
            self.load -= 1
            self.shot_time = pygame.time.get_ticks()
            if self.load == 0:
                self.load_time = pygame.time.get_ticks()
                
    def reload(self, dude, pos, check):
        self.load = 0
        self.shot

def muv(sr, pos, coord):
    x1, y1 = pos[0], pos[1]
    x, y = coord[0], coord[1]
    angle = np.arctan2((x1 - x), (y1 - y)) * 180 / np.pi
    sr1 = pygame.transform.rotate(sr, angle - 90)
    return sr1, sr1.get_size(), angle

class bullet:
    def __init__(self, pos, coord, gun):
        R = ((coord[0] - pos[0])**2 + (coord[1] - pos[1])**2)**0.5
        self.x = coord[0] + gun.h * -(coord[0] - pos[0]) / R
        self.y = coord[1] + gun.h * -(coord[1] - pos[1]) / R
        screed = pygame.Surface((3, 3))
        screed.fill(G.WHITE)
        self.angle = 3 * randint(-gun.spread, gun.spread) / 100

        self.check = True

        self.V = 100
        self.dx = self.V * -(coord[0] - pos[0]) / R
        self.dy = self.V * -(coord[1] - pos[1]) / R + self.angle
        self.dx /= self.V * 5
        self.dy /= self.V* 5
        self.damage = gun.damage
        self.image = screed
        self.mask = pygame.mask.from_surface(screed)

    def dvizh(self, coord_kako):

        self.x += self.dx
        self.y += self.dy
        self.x1 += self.dx
        self.y1 += self.dy
        pygame.draw.polygon(screen, G.GREY, ((self.x, self.y - 1), (self.x1, self.y1 - 1),
                (self.x1, self.y1 + 1), (self.x, self.y + 1)), 0)


clock = pygame.time.Clock()
finished=False


coord = [200, 405]
ch=False