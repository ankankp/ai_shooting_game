import pygame
import random
from rl_enemy import RLEnemy

# ---------------- INIT ----------------
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RL Shooting Game")
clock = pygame.time.Clock()

# ---------------- LOAD SOUND ----------------
shoot_sound = pygame.mixer.Sound("sounds/sounds.wav")
shoot_sound.set_volume(0.4)

# ---------------- BULLET ----------------
class Bullet:
    def __init__(self, x, y, dy):
        self.rect = pygame.Rect(x, y, 5, 10)
        self.dy = dy

    def move(self):
        self.rect.y += self.dy

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)

# ---------------- PLAYER ----------------
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - 60, 40, 40)
        self.health = 100
        self.bullets = []
        self.dy = -7

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.rect.x, self.rect.y - 10, 40, 5))
        pygame.draw.rect(screen, (0, 255, 0),
                         (self.rect.x, self.rect.y - 10,
                          40 * self.health / 100, 5))
        for b in self.bullets:
            b.draw()

# ---------------- GAME SETUP ----------------
player = Player()
enemy = RLEnemy(random.randint(50, WIDTH - 50), 50)

PLAYER_SPEED = 7
BULLET_LIMIT = 3

# ---------------- MAIN LOOP ----------------
running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------- STEP 3: reward init --------
    reward = -0.01

    # -------- PLAYER INPUT --------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.rect.x += PLAYER_SPEED
    if keys[pygame.K_SPACE]:
        if len(player.bullets) < BULLET_LIMIT:
            player.bullets.append(
                Bullet(player.rect.centerx, player.rect.y, player.dy)
            )
            shoot_sound.play()  # 🔊 SHOOT SOUND

    player.rect.x = max(0, min(WIDTH - 40, player.rect.x))

    # -------- PLAYER BULLETS --------
    for b in player.bullets[:]:
        b.move()
        if b.rect.colliderect(enemy.rect):
            enemy.health -= 10
            reward -= 10
            shoot_sound.play()  # 🔊 HIT SOUND
            player.bullets.remove(b)
        elif b.rect.y < 0:
            player.bullets.remove(b)

    # -------- ENEMY ACTION (RL) --------
    enemy_action, state = enemy.act(player)
    enemy.apply_action(enemy_action)

    # -------- ENEMY BULLETS --------
    for b in enemy.bullets[:]:
        b.y += 7
        if b.colliderect(player.rect):
            player.health -= 10
            reward += 10
            shoot_sound.play()  # 🔊 HIT SOUND
            enemy.bullets.remove(b)
        elif b.y > HEIGHT:
            enemy.bullets.remove(b)

    # -------- STEP 4: learning --------
    next_state = enemy.get_state(player)
    enemy.agent.remember(state, enemy_action, reward, next_state)
    enemy.agent.train()

    if pygame.time.get_ticks() % 2000 == 0:
        enemy.agent.update_target()

    # -------- DRAW --------
    player.draw()
    pygame.draw.rect(screen, (255, 0, 0), enemy.rect)

    pygame.display.update()
    clock.tick(60)

    # -------- GAME OVER --------
    if player.health <= 0 or enemy.health <= 0:
        running = False

pygame.quit()