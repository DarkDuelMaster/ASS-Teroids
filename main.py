import pygame
from constants import *
from circleshape import *
from player import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
        			return
		dt = clock.tick(60)/1000
		screen.fill("black")
		player1.update(dt)
		player1.draw(screen)
		pygame.display.flip()


if __name__ == "__main__":
    main()


