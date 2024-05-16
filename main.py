import time
import renderer
import pygame
import grid_system
import algorythms

GRID_HEIGHT, GRID_WIDTH = (10, 10)

def WriteGrid(grid):

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            print(grid[x][y], end = "  ")
        
        print("")

def main():

    # Initialisation de Pygame
    pygame.init()

    # Définition des dimensions de la fenêtre
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    
    grid = grid_system.GridInit(GRID_WIDTH,GRID_HEIGHT)
    grid[1][1] = 1
    grid[1][2] = 1
    grid[1][3] = 1

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        grid = algorythms.Conway(grid, GRID_WIDTH, GRID_HEIGHT)

        # Efface l'écran
        renderer.ClearScreen(screen)

        # Dessine la grille
        renderer.DrawGrid(grid, GRID_WIDTH, GRID_HEIGHT, screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    
        # Mise à jour de l'affichage
        pygame.display.flip()

        time.sleep(0.1)

# Quitter Pygame
pygame.quit()

if __name__ == '__main__':
    main()