import pygame as pg
import random, time, sys
from pygame.locals import *

pg.init()

font = pg.font.SysFont("Areal", 60)
font_small = pg.font.SysFont("Verdana", True, 20)

# display settings
sc = pg.display.set_mode((1000, 1000))
W, H = 1000, 1000
pg.display.set_caption("RACER")
clock = pg.time.Clock()


# materials loading
bgRoad = pg.image.load("Lab9/images/bgRoad.png")
sharkIm = pg.image.load("Lab9/images/Player.png")
rocketIm = pg.image.load("Lab9/images/rocket.jpg")
bombIm = pg.image.load("Lab9/images/bomb.jpg")


# settings
speed = 3
game_over = font.render("Game Over", True, (0, 0, 0))
score = 100
money = 0
index = 0
x = 20
y = 20


# class of enemy
class Cherry(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Lab9/images/cherry.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 10

    def move(self):
        global money
        self.rect.move_ip(0, 3)
        if self.rect.top > 1100:
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, W - 40), 200)

    def draw(self):
        sc.blit(self.image, self.rect)


# class of enemy
class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Lab9/images/coin.png")
        self.rect = self.image.get_rect()
        self.speed = 7

    def move(self):
        global money
        self.rect.move_ip(0, self.speed)
        if self.rect.top > 1000:
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, W - 40), 200)

    def draw(self):
        sc.blit(self.image, self.rect)


# class of dangereous enemy
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Lab9/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 220)

    # movement settings
    def move(self):
        global score
        global index

        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect.move_ip(0, speed)
        if self.rect.top > 1000:
            index += 1
            score += 100 * index * 0.1
            self.rect.bottom = 0
            x = 20
            y = 20
            self.rect.center = (random.randint(40, W - 40), 200)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# class of player
class Shark(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Lab9/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 700)

    def move(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.top > 5:
            if pressed_keys[pg.K_UP]:
                self.rect.move_ip(0, -15)
        if self.rect.bottom < 1200:
            if pressed_keys[pg.K_DOWN]:
                self.rect.move_ip(0, 15)
        if self.rect.left > 0:
            if pressed_keys[pg.K_LEFT]:
                self.rect.move_ip(-15, 0)
        if self.rect.right < 1000:
            if pressed_keys[pg.K_RIGHT]:
                self.rect.move_ip(15, 0)


rocket = Enemy()
shark = Shark()
coin = Coin()
cherry = Cherry()

cherrys = pg.sprite.Group()
cherrys.add(cherry)

coins = pg.sprite.Group()
coins.add(coin)

rockets = pg.sprite.Group()
rockets.add(rocket)

group = pg.sprite.Group()
group.add(rocket, shark, coin, cherry)

speed_incr = pg.USEREVENT + 1
pg.time.set_timer(speed_incr, 2000)


run = True
while True:

    for event in pg.event.get():
        if event.type == speed_incr:
            speed += money / 20
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    sc.blit(bgRoad, (0, 0))
    scores = font.render(str(int(score)), True, (0, 0, 0))
    sc.blit(scores, (20, 20))
    monCount = font.render(str(money), True, (255, 200, 50))

    pg.mixer.music.load("Lab9/sounds/bgMusic.mp3")
    pg.mixer.music.play()

    sc.blit(monCount, (800, 10))

    for entity in group:
        sc.blit(entity.image, entity.rect)
        entity.move()

    if pg.sprite.spritecollideany(shark, coins):
        money += 1
        coin.rect.top = 1000

    if pg.sprite.spritecollideany(shark, cherrys):
        money += 2
        cherry.rect.top = 1000

    for rocket in rockets:
        if shark.rect.collidepoint(rocket.rect.center):
            sc.fill((9, 1, 1))
            sc.blit(pg.image.load("Lab9/images/tutu.jpg"), (00, 0))
            pg.mixer.music.pause()
            time.sleep(4)

            pg.display.update()
            for entity in group:
                entity.kill()
            pg.quit()
            sys.exit()

    pg.display.update()
    clock.tick(60)
