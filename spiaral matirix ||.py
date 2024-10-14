last_li = []


def create_spiral_move(matrix, richtung, i , j):
    if richtung == 'r':
        if matrix[i][j] == 0:
            return
        elif j+1 >= len(matrix[i]) or matrix[i][j+1] == 0:
            last_li.append(matrix[i][j])
            matrix[i][j] = 0
            richtung = 'd'
            i += 1
            create_spiral_move(matrix, richtung, i, j)
        else:
            last_li.append(matrix[i][j])
            matrix[i][j] = 0
            j += 1
            create_spiral_move(matrix, richtung, i, j)
    elif richtung == 'd':
        if matrix[i][j] == 0:
            return
        if i+1 >= len(matrix) or matrix[i+1][j] == 0:
            last_li.append(matrix[i][j])
            matrix[i][j] = 0
            richtung = 'l'
            j -= 1
            create_spiral_move(matrix, richtung, i, j)
        else:
            last_li.append(matrix[i][j])
            matrix[i][j] = 0
            i += 1
            create_spiral_move(matrix, richtung, i, j)
        
    elif richtung == 'l':
        if matrix[i][j] == 0:
            return
        if j-1 <= -1 or matrix[i][j-1] == 0:
            last_li.append(matrix[i][j])
            matrix[i][j] = 0
            richtung = 'u'
            i -= 1
            create_spiral_move(matrix, richtung, i, j)
        else:
            last_li.append(matrix[i][j])
            matrix[i][j] = 0
            j -= 1
            create_spiral_move(matrix, richtung, i, j)
    elif richtung == 'u':
        if matrix[i][j] == 0:
            return
        if i-1 <= -1 or matrix[i-1][j] == 0:
            last_li.append(matrix[i][j])
            matrix[i][j] = 0
            richtung = 'r'
            j += 1
            create_spiral_move(matrix, richtung, i, j)
        else:
            last_li.append(matrix[i][j])
            matrix[i][j] = 0
            i -= 1
            create_spiral_move(matrix, richtung, i, j)

first_matrix = [[1,2,3], [8,9,4], [7,6,5]]
second_matrix = [[1,2,3,4], [12,13,14,5], [11,16,15,6], [10,9,8,7]]
third_matrix = [[1,2,3,4], [8,7,6,5]]
vier_matrix = [[1,2,3,4], [10,11,12,5], [9,8,7,6]]

create_spiral_move(vier_matrix, 'r', 0, 0)
print(last_li)