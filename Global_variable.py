import pygame

import Surfaces as S
import Gun_class as Gn

g = 1
bullets = []
screen = pygame.display.set_mode((1200, 700))
FPS = 144

RED = (255, 0, 0)  # блок задания цветовой палитры
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (200, 200, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]