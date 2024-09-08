import pygame
from circleshape import *
from constants import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.reload = 0
        self.score = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        # print(a, b, c)
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.reload -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.reload <= 0:
                self.shoot()

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0, 1)
        bullet.velocity = bullet.velocity.rotate(self.rotation)
        bullet.velocity += bullet.velocity * PLAYER_SHOOT_SPEED
        self.reload = PLAYER_RELOAD

    def point(self):
        self.score += 1