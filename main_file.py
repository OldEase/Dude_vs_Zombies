import pygame
import Surfaces as S
import Classes as C
import Functions as F
import Global_variable as G
import Zombies_class as Z
import Starting_functions

pygame.init()
FPS = 144  # число кадров в секунду

pygame.mixer.music.load('ost.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

dude = C.Dude(400, 350, 0, 0, 10/FPS*30, 5, 1, 0, 100, 0, S.surface_of_dude_left)
button_shop = C.Button_objects(1100, 0, S.shop_button)
zombie = Z.Zombie(100, 350, 3/FPS*30, 10, 100, 10, 1, 1, S.surface_of_zombie_right)

shop, shop_window = Starting_functions.create_shop()

pygame.display.update()
clock = pygame.time.Clock()
shop_open = False
finished = False
time = 0

while (not finished) and (time < 100000):  # основной цикл программы
	clock.tick(FPS)
	G.screen.fill(G.LIGHT_YELLOW)
	dude = F.move_object(dude)
	zombie.follow(dude)
	zombie = F.move_object(zombie)
	F.draw_object(dude)
	F.draw_object(button_shop)
	F.draw_object(zombie)
	for event in pygame.event.get():  # блок обработки выполненных игроком действий
		shop_open, finished = F.handle_events(event, shop_open,  finished)
	dude.handle_pressing_keys(time, G.g/FPS*30)
	pos = pygame.mouse.get_pos()
	if dude.x < pos[0]:
		dude.image = S.surface_of_dude_right
	else:
		dude.image = S.surface_of_dude_left
	if shop_open:
		G.screen.blit(shop_window, (400, 150))
	time += 1
	pygame.display.update()
	G.screen.fill(G.BLACK)

pygame.quit()