import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, other):
        distance = self.position.distance_to(other.position)
        if distance <= (self.radius + other.radius):
            return True
        return False
    
    def wrap_around(self):
        if self.position.y <= (0 - self.radius):
            self.position.y = 720 + self.radius
        elif self.position.y >= (720 + self.radius):
            self.position.y = 0 - self.radius
        if self.position.x <= (0 - self.radius):
            self.position.x = 1280 + self.radius
        elif self.position.x >= (1280 + self.radius):
            self.position.x = 0 - self.radius