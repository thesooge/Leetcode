arr = ["a","b","a"]
k = 3

arr_dict = {}

for i in arr:
    if i in arr_dict:
        arr_dict[i] += 1
    else:
        arr_dict[i] = 1    
a = 0
for j in arr_dict:
    if arr_dict[j] == 1:
        a += 1
        if a == k:
            print(j)
            break
        


