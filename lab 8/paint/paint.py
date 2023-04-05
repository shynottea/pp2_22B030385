import pygame
import sys

pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont(None, 20)

selected_tool = "circle"
selected_color = (0, 0, 0)

radius = 10

def draw_rect():
    pygame.draw.rect(screen, selected_color, pygame.Rect(mouse_pos, (50, 50)))

def draw_circle():
    pygame.draw.circle(screen, selected_color, mouse_pos, 25)

def erase():
    pygame.draw.circle(screen, (255, 255, 255), mouse_pos, 25)

def draw():
    global selected_tool
    if pygame.key.get_pressed()[pygame.K_TAB]:  # TAB pressed
        pygame.draw.circle(screen, selected_color, mouse_pos, radius)
    elif selected_tool == "circle":
        pygame.draw.circle(screen, selected_color, mouse_pos, radius)
    elif selected_tool == "rect":
        draw_rect()
    elif selected_tool == "eraser":
        erase()

def handle_tool_selection():
    global selected_tool
    if event.key == pygame.K_q:
        selected_tool = "circle"
    elif event.key == pygame.K_w:
        selected_tool = "rect"
    elif event.key == pygame.K_e:
        selected_tool = "eraser"

def handle_color_selection():
    global selected_color
    if event.key == pygame.K_1:
        selected_color = (255, 0, 0)    # red
    elif event.key == pygame.K_2:
        selected_color = (0, 255, 0)    # green
    elif event.key == pygame.K_3:
        selected_color = (0, 0, 255)    # blue
    elif event.key == pygame.K_4:
        selected_color = (255, 255, 0)  # yellow
    elif event.key == pygame.K_5:
        selected_color = (255, 0, 255)  # magenta
    elif event.key == pygame.K_6:
        selected_color = (0, 255, 255)  # cyan

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                radius += 1
            elif event.button == 5:
                radius -= 1
        elif event.type == pygame.KEYDOWN:
            handle_tool_selection()
            handle_color_selection()
    screen.fill((255, 255, 255))
    mouse_pos = pygame.mouse.get_pos()
    draw()
    instructions = font.render("Press Q for Circle, W for Rectangle, E for Eraser", True, (0, 0, 0))
    color_instructions = font.render("Press 1 for Red, 2 for Green, 3 for Blue, 4 for Yellow, 5 for Magenta, 6 for Cyan", True, (0, 0, 0))
    screen.blit(instructions, (10, 10))
    screen.blit(color_instructions, (10, 30))
    pygame.display.update()