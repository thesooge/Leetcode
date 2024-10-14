s = "abccccdd"
data = {}

li_of_palind = []

for char in s: 
    data[char] = 0

for char in s:
    if char in data:
        data[char] += 1

last_odd = 0
odd_exist = False

for i in data: 
    if data[i] % 2 != 0:
        odd_exist = True
        li_of_palind.append(data[i]-1)
    else:
        li_of_palind.append(data[i])
        

if odd_exist:
    print(sum(li_of_palind) + 1)
else: 
    print(sum(li_of_palind))    
