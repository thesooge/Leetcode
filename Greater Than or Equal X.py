nums = [3,6,7,7,0]


for x in range(0, len(nums)+1):
    counter = 0
    for i in nums:
        if i >= x: 
            counter += 1 

    print(x)
    print(counter)
    print()
    if counter == x: 
        print(x)
        break        

if counter == 0:
    print(-1)    

