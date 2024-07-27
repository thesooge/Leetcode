s = "aa"
t = "a"
for i in s:
    if i in t: 
        t = t.replace(t[t.index(i)], '', 1)
        s = s.replace(s[s.index(i)], '', 1)
        


if t == '' and s == '':
    print(True)
else:
    print(False)
