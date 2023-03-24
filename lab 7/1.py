import pygame
import math
import datetime

pygame.init()
clock = pygame.time.Clock()

display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Clock")

min = pygame.image.load(r'lab 7\clock\minutes.png')
minrect = min.get_rect()
minrect.center=(400,400)

sec = pygame.image.load(r'lab 7\clock\seconds.png')
secrect = sec.get_rect()
secrect.center=(400,400)


def print_text(text, position):
    font = pygame.font.SysFont("Garamond", 40, True, False)
    surface = font.render(text, True, (0, 0, 0))
    display.blit(surface, position)

def convert_degrees_to_pygame(R, angle):
    y = math.cos(2*math.pi*angle/360)*R
    x = math.sin(2*math.pi*angle/360)*R
    return x+400-10, -(y-400)-20

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = datetime.datetime.now()
    seconds = current_time.second
    minutes = current_time.minute
    seconds -= 30
    minutes -= 15

    display.fill((255, 255, 255))

    pygame.draw.circle(display, (0, 0, 0), (400, 400), 400, 5)
    
    for number in range(1, 13):
        print_text(str(number), convert_degrees_to_pygame(380, number*30))

    sec1=pygame.transform.rotate(sec, -1*(6*seconds+180))
    secrec1=sec1.get_rect()
    secrec1.center=secrect.center
    display.blit(sec1, secrec1)

    min1=pygame.transform.rotate(min, -1*(6*minutes))
    minrec1=min1.get_rect()
    minrec1.center=minrect.center
    display.blit(min1, minrec1)
    
    pygame.display.update()
    clock.tick(60)