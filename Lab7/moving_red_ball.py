import pygame
pygame.init()

W, H = 600, 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("My first pygame project!")
pygame.display.set_icon(pygame.image.load("Lab7/images/2024-03-16.png"))

clock = pygame.time.Clock()
FPS = 60

x = W // 2
y = H // 2
radius = 25
speed = 20

flUp = flDown = flLeft = flRight = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
            elif event.key == pygame.K_UP:
                flUp = True
            elif event.key == pygame.K_DOWN:
                flDown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                flLeft = False
            elif event.key == pygame.K_RIGHT:
                flRight = False
            elif event.key == pygame.K_UP:
                flUp = False
            elif event.key == pygame.K_DOWN:
                flDown = False
                
    if flLeft and x - speed >= radius:
        x -= speed
    if flRight and x + speed <= W - radius:
        x += speed
    if flUp and y - speed >= radius:
        y -= speed
    if flDown and y + speed <= H - radius:
        y += speed
    
    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), radius)
    pygame.display.update()
            
    clock.tick(FPS)