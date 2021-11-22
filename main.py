import pygame
import Surfaces as S
import Classes as C
import Functions as F
import Global_variable as G

v = 5
pygame.init()

FPS = 30

dude = C.Dude(400, 350, 0, 0, S.surface_of_dude)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
time = 0

while (not finished) and (time < 1000): # основной цикл программы
	clock.tick(FPS)
	dude = F.move_object(dude)
	F.draw_object(dude)
	for event in pygame.event.get(): # блок обработки выполненных игроком действий
		finished = F.handle_events(event, finished)
	dude.handle_pressing_keys(v)
	time += 1
	pygame.display.update()
	G.screen.fill(G.BLACK)

pygame.quit()