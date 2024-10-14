arr1 = [2,3,1,3,2,4,6,7,9,2,19]

arr2 = [2,1,4,3,9,6]

sum_arr = []

res_arr = []

for i in range(len(arr1)):
    
    if arr1[i] not in arr2:
        sum_arr.append(arr1[i])

for z in range(len(arr2)): 
    for _ in range(arr1.count(arr2[z])):
        res_arr.append(arr2[z])    

sum_arr = sorted(sum_arr)

res_arr += sum_arr

print(res_arr)