from copy import deepcopy
import random


def Conway(grid, grid_width, grid_height):
    oldGen = deepcopy(grid)
    newGen = deepcopy(grid)

    #Iterate through every cell
    for y in range(grid_height):
        for x in range(grid_width):

            #Count the number of alive neighbors (In the most professional way ever)
            alive_neighbors = 0

            if x > 0 and y < grid_height - 1 and oldGen[x-1][y+1] == 1: alive_neighbors += 1
            if y < grid_height - 1 and oldGen[x][y+1] == 1: alive_neighbors += 1
            if x < grid_width - 1 and y < grid_height - 1 and oldGen[x+1][y+1] == 1: alive_neighbors += 1
            if x < grid_width - 1 and oldGen[x+1][y] == 1: alive_neighbors += 1
            if x < grid_width - 1 and y > 0 and oldGen[x+1][y-1] == 1: alive_neighbors += 1
            if y > 0 and oldGen[x][y-1] == 1: alive_neighbors += 1
            if x > 0 and y > 0 and oldGen[x-1][y-1] == 1: alive_neighbors += 1
            if x > 0 and oldGen[x-1][y] == 1: alive_neighbors += 1
            
            #Apply Conway's Game of Life rules (With again, amazing coding skills)

            #Any live cell with fewer than two live neighbors dies, as if by underpopulation.
            if oldGen[x][y] == 1 and alive_neighbors < 2:
                newGen[x][y] = 0

            #Any live cell with two or three live neighbors lives on to the next generation.
            if oldGen[x][y] == 1 and (alive_neighbors == 2 or alive_neighbors == 3):
                newGen[x][y] = 1

            #Any live cell with more than three live neighbors dies, as if by overpopulation.
            if oldGen[x][y] == 1 and alive_neighbors > 3:
                newGen[x][y] = 0
            
            #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            if oldGen[x][y] == 0 and alive_neighbors == 3:
                newGen[x][y] = 1
    
    return newGen

def DLA(grid, grid_width, grid_height):
    oldGrid = deepcopy(grid)
    newGrid = deepcopy(grid)

    x, y = (0, 0)

    search = True
    navigate = True

    while search:
        rand_x = random.randint(0, grid_width - 1)
        rand_y = random.randint(0, grid_height - 1)

        if oldGrid[rand_x][rand_y] == 0:
            x = rand_x
            y = rand_y

            search = False
            break
        else:
            pass
    
    while navigate:
        alive_neighbors = 0

        if y < grid_height - 1 and oldGrid[x][y+1] == 1: alive_neighbors += 1
        if x < grid_width - 1 and oldGrid[x+1][y] == 1: alive_neighbors += 1
        if y > 0 and oldGrid[x][y-1] == 1: alive_neighbors += 1
        if x > 0 and oldGrid[x-1][y] == 1: alive_neighbors += 1

        if alive_neighbors > 0:
            navigate = False
            newGrid[x][y] = 1
            break

        dir = random.randint(1, 4)

        if dir == 1:
            if y > 0: 
                y -= 1
            else:
                pass
        if dir == 2:
            if x < grid_width - 1: 
                x += 1
            else:
                pass
        if dir == 3:
            if y < grid_height - 1: 
                y += 1
            else:
                pass
        if dir == 4:
            if x > 0: 
                x -= 1
            else:
                pass

    return newGrid

def FallingSand(grid, grid_width, grid_height):
    oldGrid = deepcopy(grid)
    newGrid = deepcopy(grid)

def main():
    print("This is a library. It has:")
    print(" - Conway(grid, grid_width, grid_height): Returns a 2D list that has gone through Conway's Game of Life algorythm.")
    print(" - DLA(grid, grid_width, grid_height): Returns a 2D list that has gone through one step of Diffusion Limited Aggregation.")


if __name__ == '__main__':
    main()