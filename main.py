import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")

print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
black = (0, 0, 0)

while True:
    screen.fill(black)
    pygame.display.flip()



if __name__ == "__main__":
    main()




