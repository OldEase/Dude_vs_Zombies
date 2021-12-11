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

car = C.Car(500, 372, 0, 0, False, 20, S.surface_of_car)
dude = C.Dude(550, 350, 0, 0, 10/FPS * 30, 5, 1, 0, 100, [0] * 10, 0, car, S.surface_of_dude_left)
button_shop = [C.Button_objects(1100, 0, S.shop_button), C.Button_objects(1100, 0, S.shop_close_button)]
zombie = Z.Zombie(100, 350, 3/FPS*30, 10, 100, 10, 1, 1, S.surface_of_zombie_right)
rabbit = Z.Rabbit(200, 388, 5/FPS*30, 10, 100, 10, 1, 1, S.surface_of_rabbit_left)
shop = Starting_functions.create_shop()
gun = Gn.gun(S.surface_of_pistol, speed=1000, damage=1, magaz=10, reload=5000, amount=1, spread=10)
coord = [560, 370]
pygame.display.update()
clock = pygame.time.Clock()
finished = False
result = 'ПОРАЖЕНИЕ'
time = 0
background = C.Background(S.surface_background)

Mask_zombie = pygame.mask.from_surface(zombie.image)
Mask_dude = pygame.mask.from_surface(dude.image)

while (not finished) and (time < 100000):  # основной цикл программы
	clock.tick(FPS)
	'''if(Mask_dude.overlap_area(Mask_zombie, (int(zombie.x - dude.x), int(zombie.y - dude.y)))) != 0:
		print((int(zombie.x - dude.x), int(zombie.y - dude.y)))'''
		#zombie.image.fill(G.BLACK)
	events = pygame.event.get()
	G.screen.fill(G.LIGHT_YELLOW)
	dude = F.move_object(dude, dude)
	dude.car = F.move_object(car, dude)
	background = F.move_object(background, dude)
	F.draw_object(background)
	for bull in G.bullets:
		bull = F.move_object(bull, dude)
		F.draw_object(bull)
		if (zombie.mask.overlap_area(bull.mask, (int(zombie.x - bull.x), int(zombie.x - bull.x)))) != 0:
			print(zombie.mask.overlap(
				bull.mask, (int(zombie.x - bull.x), int(zombie.x - bull.x))))
			
	zombie.follow(dude)
	rabbit.follow(dude)
	zombie = F.move_object(zombie, dude)
	rabbit = F.move_object(rabbit, dude)
	F.draw_object(dude.car)
	F.draw_object(dude)
	F.draw_object(zombie)
	F.draw_object(rabbit)
	pos = pygame.mouse.get_pos()
	sr1, coord_change, angel = Gn.muv(gun.image, pos, coord)

	for event in events:  # блок обработки выполненных игроком действий
		shop['open'], finished = F.handle_events(event, shop['open'], finished)
		# if (event.type == pygame.MOUSEBUTTONDOWN) and (not shop['open']):
			# gun.shot(dude, pos, True, False)
	dude.handle_pressing_keys(shop['open'], time, G.g / FPS * 30)
	gun.shot(dude, pos, pygame.mouse.get_pressed()[0])
	
	sr1.set_colorkey(G.WHITE)
	G.screen.blit(sr1, (dude.x + 10 - coord_change[0] / 2, dude.y + 10 - coord_change[1] / 2))
	if dude.x < pos[0]:
		dude.image = S.surface_of_dude_right
		gun.image = S.surface_of_pistol
	else:
		dude.image = S.surface_of_dude_left
		gun.image = S.surface_of_pistol_up
	if shop['open']:
		G.screen.blit(shop['image'].image, (shop['image'].x, shop['image'].y))
		for event in events:  # блок обработки выполненных игроком в магазине действий
			C.Dude = F.shop_actions(event, shop, C.Dude)
		F.draw_object(button_shop[1])
	else:
		F.draw_object(button_shop[0])

	result, finished = F.checking_of_repairing(dude.car.repair_level, result, finished)

	time += 1
	pygame.display.update()
	G.screen.fill(G.BLACK)
print(result)
pygame.quit()
