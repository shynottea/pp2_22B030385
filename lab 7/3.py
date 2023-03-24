import pygame

pygame.init()
clock = pygame.time.Clock()

size = (500, 500)
x = 250
y = 250
radius = 25
color = (255, 0, 0)
screen = pygame.display.set_mode((size))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and y <= size[1]-radius:
            y += 20
        if keys[pygame.K_UP] and y >= radius:
            y -= 20
        if keys[pygame.K_RIGHT] and x <= size[0]-radius:
            x += 20
        if keys[pygame.K_LEFT] and x >= radius:
            x -= 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), radius)
    clock.tick(60)
    pygame.display.flip()