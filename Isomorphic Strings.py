s = "paper"
t = "title"

tmp_dict = {}
counter = 1

for i in range(len(s)):

    if s[i] in tmp_dict.keys():
        tmp_dict[s[i]+f'{i}'] = tmp_dict[s[i]]
        continue
    else: 
        tmp_dict[s[i]] = counter
        counter += 1

tmp_dict2 = {}
counter2 = 1

for i in range(len(t)):

    if t[i] in tmp_dict2.keys():
        tmp_dict2[t[i]+f'{i}'] = tmp_dict2[t[i]]

        continue
    else: 
        tmp_dict2[t[i]] = counter2
        counter2 += 1
print(tmp_dict)
print(tmp_dict2)



if list(tmp_dict.values()) == list(tmp_dict2.values()):
    print(True)
else:
    print(False)    
