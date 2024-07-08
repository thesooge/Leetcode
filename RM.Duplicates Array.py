
nums = [0,0,1,1,1,2,2,3,3,4]
k = 1

# new = list(set(nums))
# print(len(new))
for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        nums[k] = nums[i]
        k += 1

print(k)            



# for i in range(len(new_nums)- 1, -1, -1):
#     if isinstance(new_nums[i], int):
#         valid_li.insert(0, new_nums[i])
#         counter += 1
#     if isinstance(new_nums[i], str):
#         valid_li.insert(len(valid_li), new_nums[i])


