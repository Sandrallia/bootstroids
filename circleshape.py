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
        #print(f"Position: {self.position}, Velocity: {self.velocity}, Radius: {self.radius}")

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other_shape):
        min_distance = self.radius + other_shape.radius
        distance = self.position.distance_to(other_shape.position)
        if distance <= min_distance:
            return True
        if distance >= min_distance:
            return False