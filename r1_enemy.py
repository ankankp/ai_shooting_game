import pygame
from agent import DQNAgent

WIDTH, HEIGHT = 800, 600
SPEED = 5
BULLET_LIMIT = 3

class RLEnemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.health = 100
        self.bullets = []
        self.agent = DQNAgent()

    def get_state(self, player):
        return [
            self.rect.x / WIDTH,
            player.rect.x / WIDTH,
            self.health / 100,
            player.health / 100
        ]

    def act(self, player):
        state = self.get_state(player)
        action = self.agent.act(state)
        return action, state

    def apply_action(self, action):
        if action == 0:          # move left
            self.rect.x -= SPEED

        elif action == 1:        # move right
            self.rect.x += SPEED

        elif action == 2 and len(self.bullets) < BULLET_LIMIT:  # shoot
            self.bullets.append(
                pygame.Rect(self.rect.centerx, self.rect.bottom, 5, 10)
            )
        # action == 3 → do nothing

        # keep enemy inside screen
        self.rect.x = max(0, min(WIDTH - 40, self.rect.x))