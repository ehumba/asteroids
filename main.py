import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *


def main():
    pygame.init()
    print("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    field = AsteroidField()
    frames = pygame.time.Clock()
    dt = 0

    

    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print('Game Over!')
                sys.exit()
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision(bullet) == True:
                    asteroid.split()
                    bullet.kill()
        pygame.display.flip()
        
        dt = frames.tick(60) / 1000
        




if __name__ == "__main__":
    main()




