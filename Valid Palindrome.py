s = "A man, a plan, a canal: Panama"
s = list(s)

for i in range(len(s)):
    if s[i].isalpha():
        if s[i].islower():
            continue
        else:
            s[i] = s[i].lower()
s = ''.join(s)

for i in s:
    if i.isalpha() or i.isdigit():
        continue
    else:
        s = s.replace(i,'')

if s == s[::-1]:
    print(True)
else:
    print(False)    
