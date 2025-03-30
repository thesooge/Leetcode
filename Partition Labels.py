s = "abaccbdeffed"
li = []

i = 0
j = 1
while i < len(s):
    tmp = s[i]
    if tmp in s[j:]:
        j += 1 
    else:
        if len(set(s[j:]).intersection(set(s[i:j]))):
            j += 1
        else:            
            li.append(len(s[i:j]))
            i = j 
            j += 1


print(li)
