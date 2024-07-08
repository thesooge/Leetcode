height = [1,1]

n = len(height)
area = 0
distance = 0

for i in range(n):
    distance = 0
    for j in range(i, n):
        distance += 1
        for z in range(1, height[j]+1):
            for x in range(n-1, i, -1):
                # print(height[x])
                for y in range (1, height[x]+1):
                
                    if y * z * distance > area:
                        area = y * z




print(area)
