nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5

for i in range(len(nums1)-1, -1, -1):
    if n == 0:
        break

    if m == 0:
        nums1[i] = nums2[n-1]
        n -= 1  

    elif nums1[m-1] > nums2[n-1]:
        nums1[i] = nums1[m-1]
        m -= 1
    else:
        nums1[i] = nums2[n-1]
        n -= 1    

print(nums1)


