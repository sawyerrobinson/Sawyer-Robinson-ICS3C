import math
import sys
import pygame

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 1000, 600
FPS = 60

# Colors
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
BLUE = (50, 100, 220)
YELLOW = (255, 215, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Rocket League - Pygame")
clock = pygame.time.Clock()


class Car:

  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.angle = 0
    self.speed = 0
    self.max_speed = 6
    self.boost = 100
    self.color = color
    self.width = 40
    self.height = 24
    self.turn_speed = 4.5

  def handle_keys(
      self, keys, left_key, right_key, forward_key, back_key, boost_key
  ):
    # Turning
    if keys[left_key]:
      self.angle += self.turn_speed
    if keys[right_key]:
      self.angle -= self.turn_speed

    # Acceleration / Reverse
    accel = 0.2
    if keys[forward_key]:
      is_boosting = keys[boost_key] and self.boost > 0
      if is_boosting:
        accel = 0.45
        self.max_speed = 10
        self.boost = max(0, self.boost - 0.8)
      else:
        self.max_speed = 6

      self.speed += accel
      if self.speed > self.max_speed:
        self.speed = self.max_speed
    elif keys[back_key]:
      self.speed -= accel
      if self.speed < -3:
        self.speed = -3
    else:
      self.speed *= 0.95  # Friction

    # Re-fill boost slowly
    if not keys[boost_key] or self.boost <= 0:
      self.boost = min(100, self.boost + 0.15)

    # Move based on angle
    rad = math.radians(self.angle)
    self.x += math.cos(rad) * self.speed
    self.y -= math.sin(rad) * self.speed

    # Boundaries
    self.x = max(30, min(WIDTH - 30, self.x))
    self.y = max(30, min(HEIGHT - 30, self.y))

  def draw(self, surface):
    car_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
    pygame.draw.rect(
        car_surf, self.color, (0, 0, self.width, self.height), border_radius=6
    )
    pygame.draw.rect(car_surf, WHITE, (self.width - 15, 4, 8, self.height - 8))

    rotated_surf = pygame.transform.rotate(car_surf, self.angle)
    new_rect = rotated_surf.get_rect(center=(self.x, self.y))
    surface.blit(rotated_surf, new_rect.topleft)

  def get_rect(self):
    return pygame.Rect(self.x - 20, self.y - 12, 40, 24)


class Ball:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.vx = 0
    self.vy = 0
    self.radius = 14

  def update(self):
    self.x += self.vx
    self.y += self.vy
    self.vx *= 0.98
    self.vy *= 0.98

    if self.y - self.radius < 20 or self.y + self.radius > HEIGHT - 20:
      self.vy *= -1
      self.y = max(20 + self.radius, min(HEIGHT - 20 - self.radius, self.y))

    goal_top = HEIGHT / 2 - 70
    goal_bottom = HEIGHT / 2 + 70

    if self.x - self.radius < 20:
      if goal_top < self.y < goal_bottom:
        return "BLUE_SCORE"
      else:
        self.vx *= -1
        self.x = 20 + self.radius

    if self.x + self.radius > WIDTH - 20:
      if goal_top < self.y < goal_bottom:
        return "RED_SCORE"
      else:
        self.vx *= -1
        self.x = WIDTH - 20 - self.radius

    return None

  def draw(self, surface):
    pygame.draw.circle(
        surface, YELLOW, (int(self.x), int(self.y)), self.radius
    )
    pygame.draw.circle(
        surface, BLACK, (int(self.x), int(self.y)), self.radius, 2
    )

  def get_rect(self):
    return pygame.Rect(
        self.x - self.radius,
        self.y - self.radius,
        self.radius * 2,
        self.radius * 2,
    )


def reset_game():
  car1.x = WIDTH * 0.25
  car1.y = HEIGHT / 2
  car1.angle = 0
  car1.speed = 0
  car1.boost = 100

  car2.x = WIDTH * 0.75
  car2.y = HEIGHT / 2
  car2.angle = 180
  car2.speed = 0
  car2.boost = 100

  ball.x = WIDTH / 2
  ball.y = HEIGHT / 2
  ball.vx = 0
  ball.vy = 0


car1 = Car(WIDTH * 0.25, HEIGHT / 2, BLUE)
car2 = Car(WIDTH * 0.75, HEIGHT / 2, RED)
ball = Ball(WIDTH / 2, HEIGHT / 2)

score_blue = 0
score_red = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()

  car1.handle_keys(
      keys, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE
  )
  car2.handle_keys(
      keys,
      pygame.K_LEFT,
      pygame.K_RIGHT,
      pygame.K_UP,
      pygame.K_DOWN,
      pygame.K_RSHIFT,
  )

  goal = ball.update()
  if goal == "BLUE_SCORE":
    score_blue += 1
    reset_game()
  elif goal == "RED_SCORE":
    score_red += 1
    reset_game()

  b_rect = ball.get_rect()
  for car in [car1, car2]:
    if car.get_rect().colliderect(b_rect):
      dx = ball.x - car.x
      dy = ball.y - car.y
      dist = math.hypot(dx, dy) or 1
      nx, ny = dx / dist, dy / dist
      hit_speed = max(4, abs(car.speed) * 1.8)
      ball.vx = nx * hit_speed
      ball.vy = ny * hit_speed

  screen.fill(GREEN)
  pygame.draw.rect(screen, WHITE, (20, 20, WIDTH - 40, HEIGHT - 40), 4)
  pygame.draw.line(
      screen, WHITE, (WIDTH / 2, 20), (WIDTH / 2, HEIGHT - 20), 2
  )
  pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 70, 2)

  goal_top = HEIGHT / 2 - 70
  goal_bottom = HEIGHT / 2 + 70
  pygame.draw.line(screen, GREEN, (20, goal_top), (20, goal_bottom), 4)
  pygame.draw.line(
      screen, GREEN, (WIDTH - 20, goal_top), (WIDTH - 20, goal_bottom), 4
  )

  car1.draw(screen)
  car2.draw(screen)
  ball.draw(screen)

  score_text = font.render(
      f"BLUE: {score_blue}   |   RED: {score_red}", True, WHITE
  )
  screen.blit(score_text, (WIDTH / 2 - score_text.get_width() / 2, 30))

  p1_boost_text = font.render(f"P1 Boost: {int(car1.boost)}%", True, BLUE)
  p2_boost_text = font.render(f"P2 Boost: {int(car2.boost)}%", True, RED)
  screen.blit(p1_boost_text, (30, HEIGHT - 40))
  screen.blit(
      p2_boost_text, (WIDTH - p2_boost_text.get_width() - 30, HEIGHT - 40)
  )

  pygame.display.flip()

pygame.quit()
sys.exit()
