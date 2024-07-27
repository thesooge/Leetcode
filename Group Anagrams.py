
strs = ["a"]
last_li = []
ddict = {}

for i in strs:
    li = [i]
    if ''.join(sorted(i)) in ddict.keys():
        ddict[''.join(sorted(i))] += li
    else:
        ddict[''.join(sorted(i))] = li

for i in ddict.values():
    last_li.append(i)
print(last_li)  
        