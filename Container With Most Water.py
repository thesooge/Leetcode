height = [1,1]

left = 0

right = len(height) - 1


max_area = 0

while left != right:
    distance = right - left
    live_area = min(height[left], height[right]) * distance

    if live_area > max_area:
        max_area = live_area

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1        


print(max_area)