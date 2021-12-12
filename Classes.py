import pygame


class Dude:
    def __init__(self, x, y, dx, dy, v, power_of_jump, a, skills, lives, guns, money, car, image, width, height):
        '''
        задаем начальные параметры элемента класса:
        x, y - координаты человечка;
        dx, dy -текущая скорость;
        v - максимальная горизонтальная скорость;
        power_of_jump - сила прыжка; a - ускорение;
        skills - очки опыта; lives - здоровье (lives = 0 означает смерть героя);
        guns - список имеющегося у игрока оружия;
        car - машины игрока
        money - кол-во монет; image - поверхность, на которой рисуется человечек
        width - ширина, height - высота поверхности
        '''
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.v = v
        self.power_of_jump = power_of_jump
        self.a = a
        self.skills = skills
        self.lives = lives
        self.guns = guns
        self.money = money
        self.car = car
        self.image = image
        self.width = width
        self.height = height

    def handle_pressing_keys(self, shop_open, time, g):
        '''
        обрабатывает нажатия на клавиши и отвечает за движение человечка
        v - максимальная скорость, а - ускорение по горизонтальной оси,
        g - по вертикальной
        '''
        # считываем данные о том, какие клавиши в данный момент зажаты
        button_left_check = - pygame.key.get_pressed()[pygame.K_LEFT]
        button_right_check = pygame.key.get_pressed()[pygame.K_RIGHT]
        button_up_check = - pygame.key.get_pressed()[pygame.K_UP]
        button_down_check = pygame.key.get_pressed()[pygame.K_DOWN]

        if (not shop_open) and (not self.car.repairing):
            # обработка движения по горизонтальной оси
            if time % (16 - self.a) == 0:
                self.dx += button_left_check + button_right_check
            if (button_right_check + button_left_check == 0) and (self.dx != 0):
                self.dx = 0

            if self.dx > self.v:  # скорость не должна превышать по  модудю значения v
                self.dx = self.v
            if self.dx < - self.v:
                self.dx = - self.v

            if (self.x <= 0) and (self.dx < 0) or (self.x >= 1200) and (self.dx > 0):
                self.dx = 0  # человечек не может выбежать за пределы экрана

            # обработка движения по вертикальной оси
            if self.car.x - self.width < self.x + self.dx < self.car.x + 40:
                level_of_ground = self.car.y - self.height
            else:
                level_of_ground = 350
            if (self.y < level_of_ground) and (self.y + self.dy > level_of_ground):
                self.dy = level_of_ground - self.y
            if self.y >= level_of_ground:
                self.dy = button_up_check * self.power_of_jump
            else:
                self.dy += g

        if not shop_open:
            # починка машины
            if (button_down_check == 1) and (self.x - 30 < self.car.x < self.x + 30):
                self.car.repairing = True
                self.car.repair_level += 1
            else:
                self.car.repairing = False

    def check_collision_with_car(self):
        if (self.x + self.width <= self.car.x) and (self.x + self.width + self.dx > self.car.x) and (
                self.y + self.dy > self.car.y - self.height) and (self.y > self.car.y - self.height):
            self.dx = self.car.x - self.width - self.x
        if (self.x >= self.car.x + 40) and (self.x + self.dx < self.car.x + 40) and (
                self.y > self.car.y - self.height) and (self.y + self.dy > self.car.y - self.height):
            self.dx = self.car.x + 40 - self.x
        if (self.y < self.car.y - self.height) and (self.y + self.dy > self.car.y - self.height) and (
                self.car.x - self.width < self.x + self.dx < self.car.x + 40):
            self.dy = self.car.y - self.height - self.y


class Car:
    def __init__(self, x, y, dx, dy, repairing, repair_level, image):
        '''
        задаем начальные параметры элемента класса:
        x, y - координаты машины;
        dx - горизонтальная скорость;
        dy - вертикальная скорость;
        image - поверхность, на которой рисуется машина
        repairing - логическая переменная, показывает, ремонтируется ли машина в настоящий момент
        repair_level - уровень починки автомобиля
        '''
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.repairing = repairing
        self.repair_level = repair_level
        self.image = image

class Button_objects:  # класс кнопок
    def __init__(self, x, y, image):
        '''
        задаем начальные параметры элемента класса:
        x, y - координаты, отвечающие за местоположение кнопки;
        image - поверхность, на которой рисуется кнопка
        '''
        self.x = x
        self.y = y
        self.image = image

class Background:
    def __init__(self, image):
        self.x = -1200
        self.y = -50
        self.image = image
        self.dx = 0
        self.dy = 0

