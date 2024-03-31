import pygame
from pygame.locals import *
import sys
import random
import time
import math

pygame.init()
z = 0
a = 400
b = 600

Monitor = pygame.display.set_mode((a, b))


BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SPEED = 5

Monitor.fill(WHITE)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)


pygame.display.set_caption("Lab8/images/AnimatedStreet.png")

class monster_car(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab8/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,560), 0)

    def move(self):
        self.rect.move_ip(1, 10) 
        if (self.rect.bottom > 600) :
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect) 


class coin(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab8/images/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,560), 0)

    def move(self):
        self.rect.move_ip(1, 10) 
        if (self.rect.bottom > 600) :
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab8/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < a:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect) 



P1 = Player()
M1 = monster_car()
C1 = coin()

monsters = pygame.sprite.Group()
monsters.add(M1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()

all_sprites.add(P1)

all_sprites.add(M1)

all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


while True :
   
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 2
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    all_sprites.update()

    
    Monitor.fill(WHITE)

   
    scores = font_small.render(str(z), True, BLACK)
    Monitor.blit(scores, (10,10))


    for entity in all_sprites:
        Monitor.blit(entity.image, entity.rect)

 

    # Check if the player car has collided with any of the monster cars
    if pygame.sprite.spritecollideany(P1, monsters):
          
        Monitor.fill(RED)
          
        pygame.display.update()
          

        for entity in all_sprites:
            entity.kill() 
                
        time.sleep(2)
        print(math.ceil(z/12))

        pygame.quit()
        sys.exit() 
          

    
    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound('Lab8/sounds/collectcoin-6075.mp3').play()
        z += 1
          
        # Update the display
        pygame.display.update()



    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
   
    P1.update()
    M1.move()
    C1.move()



    Monitor.fill(WHITE)
    P1.draw(Monitor)
    M1.draw(Monitor)
    C1.draw(Monitor)
         

        
    pygame.display.update()
    frequency = pygame.time.Clock()
    frequency.tick(60)