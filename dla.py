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

def UpdateScreen(_grid):

    # Clear screen
    renderer.ClearScreen(screen)

    # Render grid
    renderer.DrawGrid(_grid, GRID_WIDTH, GRID_HEIGHT, screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Render UI
    screen.blit(pause_text, (10, 10 + speed_text.get_height() * 0))
    screen.blit(speed_text, (10, 10 + speed_text.get_height() * 1))
    screen.blit(draw_text, (10, 10 + speed_text.get_height() * 2))

    # Update screen
    pygame.display.flip()

def UpdateScreenNoUI(_grid):

    # Clear screen
    renderer.ClearScreen(screen)

    # Render grid
    renderer.DrawGrid(_grid, GRID_WIDTH, GRID_HEIGHT, screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Update screen
    pygame.display.flip()

def main():
    # Variables init
    ticking = False
    scroll = 0
    clicked = False

    # Grid init
    grid = grid_system.GridInit(GRID_WIDTH,GRID_HEIGHT)

    # Cells init
    grid[int(GRID_WIDTH/2)][int(GRID_HEIGHT/2)] = 1

    # First frame render
    UpdateScreen(grid)

    # Main loop
    running = True
    while running:

        # Inputs ########################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:
                # Pause if spacebar pressed
                if event.key == pygame.K_SPACE:
                    ticking = not ticking

                # Screenshot if S key pressed
                if event.key == pygame.K_s:

                    # Clean screen from UI
                    UpdateScreenNoUI(grid)

                    # Take a screenshot
                    renderer.Screenshot(screen, "DLA" + str(GRID_WIDTH) + "x" + str(GRID_HEIGHT))

                    # Put UI back
                    UpdateScreen(grid)

            # Change simulation speed with mousewheel
            if event.type == pygame.MOUSEWHEEL:
                scroll += int(event.y)
                if scroll < 0: scroll = 0
                elif scroll > 10: scroll = 10

            # Draw if LMB pressed and simulation not running
            if pygame.mouse.get_pressed(num_buttons=3)[0] == True and not ticking:
                selected_pixel_x = math.floor(pygame.mouse.get_pos()[0] / PIXEL_SIZE)
                selected_pixel_y = math.floor(pygame.mouse.get_pos()[1] / PIXEL_SIZE)

                if not clicked:
                    state = grid_system.Switch(grid, selected_pixel_x, selected_pixel_y)
                try:
                    # Switch pixel state
                    grid[selected_pixel_x][selected_pixel_y] = state

                    # Add pixel on screen
                    UpdateScreen(grid)
                except:
                    pass
                clicked = True
            else:
                clicked = False
        
        # Dynamic variables
        simulation_speed = MIN_SPEED - (scroll / 10)
        
        # Simulation ######################################################
        if ticking:

            grid = algorythms.DLA(grid, GRID_WIDTH, GRID_HEIGHT)

            # Render simulation
            UpdateScreen(grid)

            time.sleep(simulation_speed)

    pygame.quit()

if __name__ == '__main__':
    main()