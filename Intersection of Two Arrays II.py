nums1 = [4,9,5]
nums2 = [9,4,9,8,4]


hash_table = {}
last_list = []
for i in nums1:
    if i in hash_table.keys():
        hash_table[i] += 1
    else:    
        hash_table[i] = 1

for j in nums2:
    if j in hash_table.keys():
        hash_table[j] -= 1
        if hash_table[j] >= 0:
            last_list.append(j)
     

print(hash_table)
print(last_list)

    
