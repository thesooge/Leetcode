s = ["h","e","l","l","o"]

empty = []

for i in range(len(s)-1, -1, -1):
    empty.append(s[i])
    s.pop(i)
s = empty + s 
print(s)    