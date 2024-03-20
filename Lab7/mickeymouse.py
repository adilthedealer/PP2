import pygame, datetime
import sys
from pygame.locals import *

# please click ESC in order to quit the pygame clock window

pygame.init()

screen_width = 1400
screen_height = 1050
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Mouse Clock")

clock_face = pygame.image.load("Lab7/mmclock/mainclock.png").convert_alpha()
minute_hand = pygame.image.load("Lab7/mmclock/rightarm.png").convert_alpha()
second_hand = pygame.image.load("Lab7/mmclock/leftarm.png").convert_alpha()


clock_center = (screen_width // 2, screen_height // 2)


def rotate(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=clock_center)
    return rotated_image, rotated_rect



clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


    current_time = datetime.datetime.now() - datetime.timedelta(minutes = 7) - datetime.timedelta(seconds=13)
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    screen.fill((255, 255, 255))

    screen.blit(clock_face, (0, 0))

    minute_angle = -minute * 6 - (second / 10) - 90
    minute_hand_rotated, minute_hand_rect = rotate(minute_hand, minute_angle)
    screen.blit(minute_hand_rotated, minute_hand_rect)

    second_angle = -second * 6 - 90
    second_hand_rotated, second_hand_rect = rotate(second_hand, second_angle)
    screen.blit(second_hand_rotated, second_hand_rect)

    pygame.display.flip()

    clock.tick(60)  # Update every second