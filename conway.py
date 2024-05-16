import math
import time
import renderer
import pygame
import grid_system
import algorythms

GRID_HEIGHT, GRID_WIDTH = (100, 100)
MIN_SPEED = 1
PIXEL_SIZE = 6

white = (252, 251, 244)
black = (20, 25, 24)
purple = (186, 85, 255)

# Pygame init
pygame.init()

# Screen init
SCREEN_WIDTH = PIXEL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = PIXEL_SIZE * GRID_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
font = pygame.font.SysFont("Classic Console Neue", 16)

#Texts init
pause_text = font.render("Space bar - pause", True, purple)
speed_text = font.render("Mousewheel - speed", True, purple)
draw_text = font.render("LMB - draw", True, purple)

def WriteGrid(grid):

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            print(grid[x][y], end = "  ")
        
        print("")

def main():
    # Variables init
    ticking = True
    scroll = 0
    clicked = False

    # Grid init
    grid = grid_system.GridInit(GRID_WIDTH,GRID_HEIGHT)

    # Cells init
    grid[1][0] = 1
    grid[2][1] = 1
    grid[2][2] = 1
    grid[1][2] = 1
    grid[0][2] = 1

    # Main loop
    running = True
    while running:

        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ticking = not ticking
            if event.type == pygame.MOUSEWHEEL:
                scroll += int(event.y)
                if scroll < 0: scroll = 0
                elif scroll > 10: scroll = 10
            if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
                selected_pixel_x = math.floor(pygame.mouse.get_pos()[0] / PIXEL_SIZE)
                selected_pixel_y = math.floor(pygame.mouse.get_pos()[1] / PIXEL_SIZE)

                if not clicked:
                    grid[selected_pixel_x][selected_pixel_y] = grid_system.Switch(grid, selected_pixel_x, selected_pixel_y)

                    # Add pixel on screen
                    renderer.ClearScreen(screen)
                    renderer.DrawGrid(grid, GRID_WIDTH, GRID_HEIGHT, screen, SCREEN_WIDTH, SCREEN_HEIGHT)
                    screen.blit(pause_text, (10, 10 + speed_text.get_height() * 0))
                    screen.blit(speed_text, (10, 10 + speed_text.get_height() * 1))
                    screen.blit(draw_text, (10, 10 + speed_text.get_height() * 2))
                    pygame.display.flip()
                
                clicked = True
            else:
                clicked = False
        
        # Dynamic variables
        simulation_speed = MIN_SPEED - (scroll / 10)
        
        if ticking:

            grid = algorythms.Conway(grid, GRID_WIDTH, GRID_HEIGHT)

            renderer.ClearScreen(screen)

            renderer.DrawGrid(grid, GRID_WIDTH, GRID_HEIGHT, screen, SCREEN_WIDTH, SCREEN_HEIGHT)

            # Render texts
            screen.blit(pause_text, (10, 10 + speed_text.get_height() * 0))
            screen.blit(speed_text, (10, 10 + speed_text.get_height() * 1))
            screen.blit(draw_text, (10, 10 + speed_text.get_height() * 2))

            pygame.display.flip()

            time.sleep(simulation_speed)

    pygame.quit()

if __name__ == '__main__':
    main()