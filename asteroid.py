import pygame
import random
from circleshape import *
from main import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        old_velocity = self.velocity
        old_radius = self.radius
        old_position = self.position
        self.kill()

        if old_radius <= ASTEROID_MIN_RADIUS:
            return

        print("test")
        random_angle = random.uniform(20, 50)
        print(random_angle)
        new_velocity_1 = old_velocity.rotate(random_angle) * 1.2
        new_velocity_2 = old_velocity.rotate(-random_angle) * 1.2
        new_radius = old_radius - ASTEROID_MIN_RADIUS

        print(new_velocity_1)
        print(new_velocity_2)

        asteroid = Asteroid(old_position.x, old_position.y, new_radius)
        asteroid.velocity = new_velocity_1
        asteroid= Asteroid(old_position.x, old_position.y, new_radius)
        asteroid.velocity = new_velocity_2
        
