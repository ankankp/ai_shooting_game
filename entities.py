import pygame

class Bullet:
    def __init__(self, x, y, dy):
        self.rect = pygame.Rect(x, y, 5, 10)
        self.dy = dy

    def move(self):
        self.rect.y += self.dy


class Shooter:
    def __init__(self, x, y, dy, agent):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.dy = dy
        self.agent = agent
        self.bullets = []
        self.health = 100
