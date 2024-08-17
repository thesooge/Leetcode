arr = [1,2,2,1,1,3]

hash_table = {}

for i in range(len(arr)):
    if arr[i] in hash_table:
        hash_table[arr[i]] += 1
    else:
        hash_table[arr[i]] = 1

free_li = []

for i in hash_table.values():
    if i in free_li:
        print(False)
    free_li.append(i)   