import pygame
import sys

pygame.init()

size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("consolas", 20)

selected_tool = "circle"
selected_color = (0, 0, 0)

radius = 25
mouse_trail = []

def draw():
    if pygame.mouse.get_pressed()[0]:
        mouse_trail.append((mouse_pos, selected_tool))
    for pos, tool in mouse_trail:
        if tool == "circle":
            pygame.draw.circle(screen, selected_color, pos, radius)
        elif tool == "square":
            pygame.draw.rect(screen, selected_color, pygame.Rect(pos, (50, 50))) 
        elif tool == "right_triangle":
            pygame.draw.polygon(screen, selected_color, [(pos[0], pos[1]), (pos[0], pos[1]+50), (pos[0]+50, pos[1]+50)])
        elif tool == "equilateral_triangle":
            pygame.draw.polygon(screen, selected_color, [(pos[0], pos[1]), (pos[0]+50, pos[1]), (pos[0]+25, pos[1]+50)])
        elif tool == "rhombus":
            pygame.draw.polygon(screen, selected_color, [(pos[0], pos[1]+25), (pos[0]+25, pos[1]), (pos[0]+50, pos[1]+25), (pos[0]+25, pos[1]+50)]) 
        elif tool == "eraser":
            pygame.draw.circle(screen, (255, 255, 255), pos, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                selected_tool = "circle"
            elif event.key == pygame.K_w:
                selected_tool = "square"
            elif event.key == pygame.K_e:
                selected_tool = "eraser"
            elif event.key == pygame.K_r:
                selected_tool = "rhombus" 
            elif event.key == pygame.K_t:
                selected_tool = "equilateral_triangle"
            elif event.key == pygame.K_y:
                selected_tool = "right_triangle"  
            elif event.key == pygame.K_1:
                selected_color = (255, 0, 0) #red
            elif event.key == pygame.K_2:
                selected_color = (0, 255, 0) # green
            elif event.key == pygame.K_3:
                selected_color = (0, 0, 255) # blue
    screen.fill((255, 255, 255))
    draw() 
    instructions = font.render("Press Q for Circle, W for Square, E for Equilateral Triangle, R for Rhombus,\nT for Equilateral triangle, Y for right triangle", True, (0, 0, 0))
    color_instructions = font.render("Press 1 for Red, 2 for Green, 3 for Blue", True, (0, 0, 0))
    screen.blit(instructions, (10, 10))
    screen.blit(color_instructions, (10, 30))
    pygame.display.update()