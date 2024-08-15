nums1 = [1,2,3]
nums2 = [2,4,6]

nums1 = list(set(nums1))
nums2 = list(set(nums2))

removed_item = []
for i in nums1:
    if i in nums2:
        nums2.remove(i)
        removed_item.append(i)

for i in removed_item:
    nums1.remove(i)

print(nums1)
print(nums2)