import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.travel_distance = 0
        self.old_position_x = 0
        self.old_position_y = 0
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.old_position_x = self.position.x
        self.old_position_y = self.position.y
        self.position += (self.velocity * dt)      
        delta_x = self.position.x - self.old_position_x
        delta_y = self.position.y - self.old_position_y
        self.travel_distance += ((delta_x ** 2) + (delta_y ** 2)) ** 0.5
        
        if self.travel_distance >= MAX_SHOT_DISTANCE:
            self.kill()