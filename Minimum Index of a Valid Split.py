
def minimumIndex(nums):
    # Find the majority element
    x = nums[0]
    count = 0
    x_count = 0
    n = len(nums)

    for num in nums:
        if num == x:
            count += 1
        else:
            count -= 1
        if count == 0:
            x = num
            count = 1

    # Count frequency of majority element
    for num in nums:
        if num == x:
            x_count += 1
            
    count = 0
    for index in range(n):
        if nums[index] == x:
            count += 1
        remaining_count = x_count - count
        if count * 2 > index + 1 and remaining_count * 2 > n - index - 1:
            return index

    return -1
                    

nums = [6,10,10,6,10,10,3,10,2,10]
print(minimumIndex(nums))
