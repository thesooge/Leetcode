def longestOnes(nums, k):
    longest_streak = 0
    left = 0
    right = 0
    while right != len(nums):
        if nums[right] == 0:
            k -= 1
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
        longest_streak = max(longest_streak, right - left + 1)
        right += 1
    
    return longest_streak

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))        