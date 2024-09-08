# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x, y, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                print(f"Player Score: {player.score}")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    player.point()
        pygame.display.flip()
        game_clock.tick(60)
        dt = game_clock.get_time() / 1000


if __name__ == "__main__":
    main()