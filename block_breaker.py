import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

# DISPLAY
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Block Breaker")
clock = pygame.time.Clock()

# MUSIC
pygame.mixer.music.load("winterfest.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# BACKGROUND PICTURE
bg_image = pygame.image.load("christmas_background1.jpg").convert()
bg_image = pygame.transform.scale(bg_image, (800, 600))

# COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (200, 16, 46)
GREEN = (40, 122, 63)

# PADDLE
paddle = pygame.Rect(340, 540, 120, 15)

# BALL
ball = pygame.Rect(390, 400, 15, 15)
ball_x = 4
ball_y = -4

score = 0
level = 1
max_level = 3
game_state = "playing"
bricks = []


# MOVE PADDLE
def move_paddle():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 6
    if keys[pygame.K_RIGHT] and paddle.right < 800:
        paddle.x += 6


# MOVE BALL
def move_ball():
    global ball_x, ball_y
    ball.x += ball_x
    ball.y += ball_y

    # Wall collisions
    if ball.left <= 0 or ball.right >= 800:
        ball_x = -ball_x
    if ball.top <= 0:
        ball_y = -ball_y

    # Paddle collision
    if ball.colliderect(paddle):
        ball_y = -abs(ball_y)


# CHECK WHEN BRICKS ARE HIT
def check_bricks():
    global score, ball_y
    for item in bricks[:]:
        brick_rect = item[0]
        if ball.colliderect(brick_rect):
            bricks.remove(item)
            ball_y = -ball_y
            score += 10
            break


def create_first_level():
    bricks.clear()
    brick_colours = [RED, GREEN, RED, GREEN, RED, GREEN, RED, GREEN]
    for i in range(8):
        brick = pygame.Rect(i * 100 + 10, 100, 80, 30)
        bricks.append([brick, brick_colours[i]])


def next_level():
    global level, ball_x, ball_y
    level += 1
    bricks.clear()
    brick_colours = [RED, GREEN, RED, GREEN, RED, GREEN, RED, GREEN]

    for row in range(level):
        for i in range(8):
            brick = pygame.Rect(i * 100 + 10, 100 + row * 40, 80, 30)
            bricks.append([brick, brick_colours[i]])

    ball.x = 390
    ball.y = 400
    ball_x = 2 + level
    ball_y = -(2 + level)
    paddle.x = 340


# DRAW EVERYTHING
def draw_game():
    screen.blit(bg_image, (0, 0))
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.rect(screen, GREEN, paddle)

    for brick in bricks:
        pygame.draw.rect(screen, brick[1], brick[0])

    font = pygame.font.SysFont(None, 35)
    text = font.render(f"Score: {score}   Level: {level}", True, WHITE)
    screen.blit(text, (20, 20))


def draw_end_screen(title, message):
    screen.blit(bg_image, (0, 0))
    font = pygame.font.SysFont(None, 65)
    small_font = pygame.font.SysFont(None, 35)

    title_text = font.render(title, True, GREEN)
    message_text = small_font.render(message, True, WHITE)

    screen.blit(title_text, (400 - title_text.get_width() // 2, 220))
    screen.blit(message_text, (400 - message_text.get_width() // 2, 320))


create_first_level()

# MAIN GAME LOOP
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_state == "level_complete":
                    next_level()
                    game_state = "playing"
                elif game_state in ("game_over", "won"):
                    level = 1
                    score = 0
                    ball.x, ball.y = 390, 400
                    ball_x = 2
                    ball_y = -2
                    paddle.x = 340
                    create_first_level()
                    game_state = "playing"

    # GAME LOGIC
    if game_state == "playing":
        move_paddle()
        move_ball()
        check_bricks()

        if len(bricks) == 0:
            if level < max_level:
                game_state = "level_complete"
            else:
                game_state = "won"

        if ball.bottom >= 600:
            game_state = "game_over"

    # DRAWING
    if game_state == "playing":
        draw_game()
    elif game_state == "level_complete":
        draw_end_screen("Level Complete!", "Press SPACE for next level")
    elif game_state == "won":
        draw_end_screen("You Won! You Saved Christmas!", "Press SPACE to play again")
    elif game_state == "game_over":
        draw_end_screen("Game Over", "Press SPACE to try again")

    pygame.display.flip()

pygame.quit()
sys.exit()
