import pygame
from constants import *
from shot import *
from circleshape import CircleShape

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shoot_timer = 0.0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		player_rotation = (PLAYER_TURN_SPEED * dt)
		self.rotation += player_rotation

	def update(self, dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(-1*dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_s]:
			self.move(-1*dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
			self.shoot()
			self.shoot_timer = PLAYER_SHOOT_COOLDOWN
		if self.shoot_timer > 0:
			self.shoot_timer -= dt
			if self.shoot_timer < 0:
				self.shoot_timer = 0


	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		initial_speed = pygame.Vector2(0,1)
		projectile = Shot(self.position.x, self.position.y)
		projectile_direction = initial_speed.rotate(self.rotation)
		projectile.velocity = PLAYER_SHOOT_SPEED*projectile_direction




