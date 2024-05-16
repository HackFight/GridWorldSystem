def GridInit(grid_width, grid_height):
    grid = [[0 for x in range(grid_width)] for y in range(grid_height)]
    return grid

def Switch(grid, x, y):
    newState = 0

    if grid[x][y] == 0: newState = 1
    elif grid[x][y] == 1: newState = 0

    return newState


def main():
    print("This is a library. It has:\n - GridInit(grid_width, grid_height): Returns a 2D list filled with 0.")


if __name__ == '__main__':
    main()