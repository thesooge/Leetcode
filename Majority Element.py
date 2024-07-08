nums = [3,2,3]

hash_table = {}

border = len(nums) / 2

for i in nums:
    if i in hash_table.keys():
        hash_table[i] += 1
    else:
        hash_table[i] = 1    


for value in hash_table.values():
    if value > border:
        position = list(hash_table.values()).index(value)
        print(list(hash_table.keys())[position])
