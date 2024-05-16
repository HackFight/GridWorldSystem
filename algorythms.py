from copy import deepcopy


def Conway(grid, grid_width, grid_height):
    oldGen = deepcopy(grid)
    nextGen = deepcopy(grid)

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
                nextGen[x][y] = 0

            #Any live cell with two or three live neighbors lives on to the next generation.
            if oldGen[x][y] == 1 and (alive_neighbors == 2 or alive_neighbors == 3):
                nextGen[x][y] = 1

            #Any live cell with more than three live neighbors dies, as if by overpopulation.
            if oldGen[x][y] == 1 and alive_neighbors > 3:
                nextGen[x][y] = 0
            
            #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            if oldGen[x][y] == 0 and alive_neighbors == 3:
                nextGen[x][y] = 1
    
    return nextGen



def main():
    print("This is a library. It has:\n - NextGen(grid, grid_width, grid_height): Returns a 2D list that has gone through Conway's Game of Life algorythm.")


if __name__ == '__main__':
    main()