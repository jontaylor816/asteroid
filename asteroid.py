import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)

        split1 = self.velocity.rotate(split_angle)
        split2 = self.velocity.rotate(-split_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_rad)
        asteroid.velocity = split1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_rad)
        asteroid.velocity = split2 * 1.2