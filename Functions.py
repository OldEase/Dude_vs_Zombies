from Global_variable import screen
import Classes
import pygame

def move_object (object):
    '''универсальная функция, отвечающая за движение любых объектов'''
    object.x += object.dx
    object.y += object.dy
    return object
def draw_object (object):
    '''универсальная функция, отвечающая за прорисовку объекта на экране'''
    screen.blit(object.image, (object.x, object.y))
def handle_events (event, finished):
    '''функция, обрабатывающая все произошедшие за временной интервал события'''
    if event.type == pygame.QUIT:  # выхода из игры
        finished = True
    return finished

