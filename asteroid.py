import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.math.Vector2(x, y)


        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_one = Asteroid(self.position, self.position, new_radius)
        new_ast_two = Asteroid(self.position, self.position, new_radius)
        new_ast_one.velocity = vector1 * 1.2
        new_ast_two.velocity = vector2 * 1.2


