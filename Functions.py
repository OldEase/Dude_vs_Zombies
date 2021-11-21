from Global_variable import screen
import Classes
import pygame

def move_object (object):
    object.x += object.dx
    object.y += object.dy
    return object
def draw_object (object):
    screen.blit(object.image, (object.x, object.y))
def handle_events (event, finished):
    if event.type == pygame.QUIT:  # выхода из игры
        finished = True
    return finished

