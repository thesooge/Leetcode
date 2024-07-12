matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

row = []
columns = []




for i in range(len(matrix)):
    if 0 in matrix[i]:
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0: 
                row.append(i)
                columns.append(j)


row = list(set(row))
columns = list(set(columns))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i in row:
            matrix[i][j] = 0
        if j in columns: 
            matrix[i][j] = 0    

print(matrix)
print(row)   
print(columns, "col")               