import Surfaces as S
import pygame
import  Global_variable as G


class Zombie():
    def __init__(self, width, height, dude, x_coord=0, y_coord=0, dx_max=4, dy_max=10,
                 lives=100, damage=10, exp=1, money=1, image=S.surface_of_zombie_right):
        self.x = x_coord
        self.y = y_coord
        self.dx_max = dx_max
        self.dy_max = dy_max
        self.dx = self.dx_max
        self.dy = 0
        self.lives = lives
        self.damage = damage
        self.exp = exp
        self.money = money
        self.image = image
        self.width = width
        self.height = height
        self.direction = 'right'
        if dude.x < self.x:
            self.image = self.image = pygame.transform.flip(self.image, 1, 0)
            self.direction = 'left'
            self.dx = -dx_max
        self.mask = pygame.mask.from_surface(image)


    def follow(self, dude):
        if dude.x < self.x and self.direction == 'right':
            self.dx = -self.dx
            self.image = self.image = pygame.transform.flip(self.image, 1, 0)
            self.image.set_colorkey(G.WHITE)
            self.direction = 'left'
            self.mask = pygame.mask.from_surface(self.image)
        if dude.x > self.x and self.direction == 'left':
            self.dx = -self.dx
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.image.set_colorkey(G.WHITE)
            self.direction = 'right'
            self.mask = pygame.mask.from_surface(self.image)


class Rabbit():
    def __init__(self, width, height, x_coord=0, y_coord=0, dx_max=4, dy_max=10,
                 lives=100, damage=10, exp=1, money=1, image=S.surface_of_rabbit_right):
        self.x = x_coord
        self.y = y_coord
        self.dx = 0
        self.dy = 0
        self.dx_max = dx_max
        self.dy_max = dy_max
        self.lives = lives
        self.damage = damage
        self.exp = exp
        self.money = money
        self.image = image
        self.width = width
        self.height = height

    def follow(self, dude):
        if dude.x < self.x:
            self.dx = -abs(self.dx_max)
            self.image = S.surface_of_rabbit_left
        if dude.x > self.x:
            self.dx = abs(self.dx_max)
            self.image = S.surface_of_rabbit_right