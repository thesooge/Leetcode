nums = [1,2,3]

res, sol = [], []

def trackback():
    if len(sol) == len(nums):
        res.append(sol[:])
        return
    
    for x in nums:
        if x not in sol:
            sol.append(x)
            trackback() # recrussion 
            sol.pop() # remove the last elemnt of the list

trackback()
print(res)
