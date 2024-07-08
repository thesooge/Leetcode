
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]


def isislandpr(grid):
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # print(grid[i][j], end="")
            if grid[i][j] == 1:
                perimeter += 4    
                if j >= 1:
                    if grid[i][j] == grid[i][j-1]:
                        perimeter -= 2
                        # print(grid[i][j])        
                if i >= 1:
                    if grid[i][j] == grid[i-1][j]:
                        perimeter -= 2
                        # print(grid[i][j])
    print(perimeter)
isislandpr(grid)