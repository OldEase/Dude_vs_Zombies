import pygame
import Surfaces as S
import Classes as C
import Functions as F
import Global_variable as G
import Zombies_class as Z
import Starting_functions
import Gun_class as Gn

pygame.init()
FPS = 144  # число кадров в секунду

pygame.mixer.music.load('ost.mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play()

dude = C.Dude(550, 350, 0, 0, 10/FPS * 30, 5, 1, 0, 100, [0] * 10, 0, S.surface_of_dude_left)
button_shop = C.Button_objects(1100, 0, S.shop_button)
zombie = Z.Zombie(100, 350, 3/FPS*30, 10, 100, 10, 1, 1, S.surface_of_zombie_right)
rabbit = Z.Rabbit(200, 388, 5/FPS*30, 10, 100, 10, 1, 1, S.surface_of_rabbit_left)
shop = Starting_functions.create_shop()
gun = Gn.gun(S.surface_of_pistol)
coord = [560, 370]
pygame.display.update()
clock = pygame.time.Clock()
finished = False
time = 0

while (not finished) and (time < 100000):  # основной цикл программы
	clock.tick(FPS)
	G.screen.fill(G.LIGHT_YELLOW)
	dude = F.move_object(dude, dude)
	for bull in G.bullets:
		bull = F.move_object(bull, dude)
		F.draw_object(bull)
	zombie.follow(dude)
	rabbit.follow(dude)
	zombie = F.move_object(zombie, dude)
	rabbit = F.move_object(rabbit, dude)
	F.draw_object(dude)
	F.draw_object(button_shop)
	F.draw_object(zombie)
	F.draw_object(rabbit)
	pos = pygame.mouse.get_pos()
	sr1, coord_change, angel = Gn.muv(gun.image, pos, coord)
	for event in pygame.event.get():  # блок обработки выполненных игроком действий
		shop['open'], finished = F.handle_events(event, shop['open'],  finished)
		if event.type == pygame.MOUSEBUTTONDOWN:
			G.bullets.append(Gn.bullet(pos, (dude.x + coord_change[0] / 2, dude.y + coord_change[1] / 2)))
	dude.handle_pressing_keys(time, G.g/FPS*30)


	sr1.set_colorkey(G.WHITE)
	G.screen.blit(sr1, (dude.x + 10 - coord_change[0] / 2, dude.y + 10 - coord_change[1] / 2))
	if dude.x < pos[0]:
		dude.image = S.surface_of_dude_right
		gun.image = S.surface_of_pistol
	else:
		dude.image = S.surface_of_dude_left
		gun.image = S.surface_of_pistol_up
	if shop['open']:
		G.screen.blit(shop['image'], (100, 100))
		for event in pygame.event.get():  # блок обработки выполненных игроком в магазине действий
			C.Dude = F.shop_actions(event, shop, C.Dude)
	time += 1
	pygame.display.update()
	G.screen.fill(G.BLACK)

pygame.quit()