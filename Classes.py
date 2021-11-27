import pygame

class Dude():
    def __init__(self, x, y, dx, dy, v, power_of_jump, a, skills, lives, money, image):
        '''
        задаем начальные параметры элемента класса:
        x, y - координаты человечка;
        dx, dy -текущая скорость;
        v - максимальная горизонтальная скорость;
        power_of_jump - сила прыжка; a - ускорение;
        skills - очки опыта; lives - здоровье (lives = 0 означает смерть героя);
        money - кол-во монет; image - поверхность, на которой рисуется человечек
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
        self.money = money
        self.image = image

    def handle_pressing_keys(self, time, g):
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

        # обработка движения по горизонтальной оси
        if time % (2 - self.a) == 0:
            self.dx += button_left_check + button_right_check
        if button_right_check == 0 and button_left_check == 0 and self.dx != 0:
            self.dx = 0

        if self.dx > self.v:  # скорость не должна превышать по  модудю значения v
            self.dx = self.v
        if self.dx < - self.v:
            self.dx = - self.v

        if (self.x <= 0) and (self.dx < 0) or (self.x >= 800) and (self.dx > 0):
            self.dx = 0  # человечек не может выбежать за пределы экрана

        # обработка движения по вертикальной оси
        if self.y >= 350:
            self.dy = button_up_check * self.power_of_jump
        else:
            self.dy += g
