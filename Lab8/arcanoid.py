import pygame
import random

pygame.init()

# Screen settings
W, H = 1200, 800
FPS = 60
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
bg = (0, 0, 0)

# Paddle settings
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball settings
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2**0.5)
ball = pygame.Rect(
    random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect
)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont("comicsansms", 40)
game_score_text = game_score_fonts.render(
    f"Your game score is: {game_score}", True, (255, 255, 255)
)
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound("Lab8/sounds/catch.mp3")


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


# Unbreakable bricks settings
block_list = [
    pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)
]
unbreakable_blocks = random.sample(block_list, k=5)  # Randomly choose 5 unbreakable bricks
color_list = [
    (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    for _ in range(10 * 4)
]

# Game over screen
losefont = pygame.font.SysFont("comicsansms", 40)
losetext = losefont.render("Game Over", True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win screen
winfont = pygame.font.SysFont("comicsansms", 40)
wintext = losefont.render("You win yay", True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Additional features
speed_increase_factor = 0.1
paddle_shrink_factor = 2
bonus_brick = pygame.Rect(
    random.choice(block_list).left, random.choice(block_list).top, 100, 50
)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(bg)

    # Drawing blocks
    for color, block in enumerate(block_list):
        pygame.draw.rect(screen, color_list[color], block)
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Collision with walls
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy

    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision with blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        if hitRect in unbreakable_blocks:
            dx, dy = detect_collision(dx, dy, ball, hitRect)# Handle collision with unbreakable bricks
        else:
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()

    # Game score
    game_score_text = game_score_fonts.render(
        f"Your game score is: {game_score}", True, (255, 255, 255)
    )
    screen.blit(game_score_text, game_score_rect)

    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    # Additional features
    if game_score % 10 == 0 and game_score != 0:  # Increase ball speed every 10 points
        ballSpeed += speed_increase_factor
    if game_score % 20 == 0 and game_score != 0:  # Shrink paddle every 20 points
        paddle.width -= paddle.width // paddle_shrink_factor
    if ball.colliderect(bonus_brick):  # Bonus brick feature
        ballSpeed += speed_increase_factor
        bonus_brick = pygame.Rect(
            random.choice(block_list).left, random.choice(block_list).top, 100, 50
        )

    pygame.display.flip()
    clock.tick(FPS)
