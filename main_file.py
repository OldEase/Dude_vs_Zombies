import pygame
import Surfaces as S
import Classes as C
import Functions as F
import Global_variable as G
import Zombies_class as Z

pygame.init()
screen = pygame.display.set_mode((1200, 700))
FPS = 30  # число кадров в секунду

dude = C.Dude(400, 350, 0, 0, 10, 10, 1, 0, 100, 0, S.surface_of_dude)
zombie = Z.Zombie(100, 350, 3, 10, 100, 10, 1, 1, S.surface_of_zombie)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
time = 0

while (not finished) and (time < 1000):  # основной цикл программы
	clock.tick(FPS)
	dude = F.move_object(dude)
	zombie.follow(dude)
	zombie = F.move_object(zombie)
	F.draw_object(dude)
	F.draw_object(zombie)
	for event in pygame.event.get():  # блок обработки выполненных игроком действий
		finished = F.handle_events(event, finished)
	dude.handle_pressing_keys(time, G.g)
	time += 1
	pygame.display.update()
	G.screen.fill(G.BLACK)

pygame.quit()