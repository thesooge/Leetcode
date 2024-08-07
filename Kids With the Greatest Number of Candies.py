candies = [2,3,5,1,3]
extraCandies = 3

last_li = []



for i in candies:
    if i + extraCandies >= max(candies):
        last_li.append(True)
    else:
        last_li.append(False)    



print(last_li)
