import pygame
from datetime import datetime
from datetime import date

# Couleurs
white = (252, 251, 244)
black = (20, 25, 24)

# Fonction pour dessiner la grille
def DrawGrid(grid, grid_width, grid_height, screen, screen_width, screen_height):
    for y in range(grid_height):
        for x in range(grid_width):
            if grid[x][y] == 1:

                square_width = screen_width/grid_width
                square_height = screen_height/grid_height
                pygame.draw.rect(screen, white, (x * square_width, y * square_height, square_width, square_height))

def ClearScreen(screen):
    screen.fill(black)