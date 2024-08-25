import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0)

    frames = pygame.time.Clock()
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        pygame.display.flip()
        frames.tick(60)
        dt = frames.tick() / 1000




if __name__ == "__main__":
    main()




