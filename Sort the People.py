names = ["Alice","Bob","Bob"]
heights = [155,185,150]

new_dict = {}

for i in range(len(names)):
    maxs = max(heights)
    max_indc = heights.index(maxs)
    new_dict[heights[max_indc]] = names[max_indc]

    heights[max_indc] = 0

print(new_dict)
print(list(new_dict.values()))    


    



