import pygame

class Dude():
    def __init__(self, x, y, dx, dy, image):
        '''задаем начальные параметры элемента класса'''
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.image = image

    def handle_pressing_keys(self, v):
        '''обрабатывает нажатия на клавиши и отвечает за движение человечка'''
        button_left_check = - pygame.key.get_pressed()[pygame.K_LEFT]
        button_right_check = pygame.key.get_pressed()[pygame.K_RIGHT]
        button_up_check = pygame.key.get_pressed()[pygame.K_UP]
        button_down_check = pygame.key.get_pressed()[pygame.K_DOWN]
        self.dx = v * (button_left_check + button_right_check)

        if self.y >= 300:
            self.dy = - button_up_check * v
        elif self.y <= 200:
            self.dy = - self.dy