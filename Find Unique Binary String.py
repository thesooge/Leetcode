

def findDifferentBinaryString(nums):
    n = len(nums)
    availbl = []
    for num in nums:
        availbl.append(num)

    for i in range(2**n):
        binary = bin(i)[2:]
    
        if len(binary) < n:
            binary += '0'*(n-len(binary))
        if str(binary) not in availbl:
            return binary


print(findDifferentBinaryString(["000","011","001"]))