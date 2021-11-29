import Surfaces as S


class Zombie():
    def __init__(self, x_coord=0, y_coord=0, dx_max=4, dy_max=10,
                 lives=100, damage=10, exp=1, money=1, image=S.surface_of_zombie_right):
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

    def follow(self, dude):
        if dude.x < self.x:
            self.dx = -abs(self.dx_max)
            self.image = S.surface_of_zombie_left
        if dude.x > self.x:
            self.dx = abs(self.dx_max)
            self.image = S.surface_of_zombie_right


class Rabbit():
    def __init__(self, x_coord=0, y_coord=0, dx_max=4, dy_max=10,
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

    def follow(self, dude):
        if dude.x < self.x:
            self.dx = -abs(self.dx_max)
            self.image = S.surface_of_rabbit_left
        if dude.x > self.x:
            self.dx = abs(self.dx_max)
            self.image = S.surface_of_rabbit_right