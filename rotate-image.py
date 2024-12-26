matrix = [[1,2,3],[4,5,6],[7,8,9]]

lnl = len(matrix)

lst = [[] for _ in range(len(matrix))]

for i in range(len(matrix)-1, -1, -1):
    for p in range(len(matrix)):
        matrix[p].append(matrix[i][p])

for p in matrix:
    del p[0 : lnl]

print(matrix)    
