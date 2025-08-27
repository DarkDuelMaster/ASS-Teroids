import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	asteroidfield = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
        			return
		dt = clock.tick(60)/1000
		screen.fill("black")
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.collision(player1):
				print ("Game over!")
				sys.exit()
			for bullet in shots:
				if asteroid.collision(bullet):
					asteroid.kill()
					bullet.kill()

		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()


if __name__ == "__main__":
    main()


