import pygame
pygame.init()
size = (700,600)
screen = pygame.display.set_mode(size)
done  = False
clock = pygame.time.Clock()
while not done:
	#--main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill((255,255,255))
	pygame.display.flip()
	clock.tick(1060)

