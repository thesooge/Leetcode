nums = [1,2,3,1]

num_dict = {}

for i in range(len(nums)):
    if nums[i] in num_dict:
        num_dict[nums[i]] += 1
        if num_dict[nums[i]] == 2:
            print(True)  
    else:
        num_dict[nums[i]] = 1



