import grid_system
import algorythms

GRID_HEIGHT, GRID_WIDTH = (10, 10)

def WriteGrid(grid):

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            print(grid[x][y], end = "  ")
        
        print("")

def main():
    
    grid = grid_system.GridInit(GRID_WIDTH,GRID_HEIGHT)
    grid[1][1] = 1
    grid[1][2] = 1
    grid[1][3] = 1

    WriteGrid(grid)
    print("")

    grid = algorythms.Conway(grid, GRID_WIDTH, GRID_HEIGHT)

    WriteGrid(grid)
    print("")

if __name__ == '__main__':
    main()