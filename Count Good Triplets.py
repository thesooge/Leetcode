arr = [7,3,7,3,12,1,12,2,3]
a = 5
b = 8
c = 1 

triple_li = []
i = 0
j = 1
k = 2

while i <= len(arr) - 3:
    for j in range(i+1, len(arr) - 1):
        for k in range(j+1, len(arr)):
            if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                triple_li.append([arr[i], arr[j], arr[k]])
    i += 1
print(len(triple_li))    