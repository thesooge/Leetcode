grid = [[1,3,1],[1,5,1],[4,2,1]]

# print(grid[2][2])


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i and j: 
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        elif not i and j: 
            grid[i][j] += grid[i][j-1]
        elif not j and i: 
            grid[i][j] += grid[i-1][j]   

print(grid)
print(grid[-1][-1])


# i, j = 0, 0

# sum = 0 

# while i != len(grid) - 1 and j != len(grid[j]) - 1:
#     try:
#         sum += min(grid[i][j+1], grid[i+1][j])




#     except: 

#         continue

#     # i += 1 
#     # j += 1 
