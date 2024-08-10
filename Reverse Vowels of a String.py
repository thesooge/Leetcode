s = "aA"

vowel_li = ['a', 'e', 'i', 'o', 'u']
s = list(s)

i = 0
j = len(s) - 1

while i < j:
    if s[i].lower() in vowel_li and s[j].lower() in vowel_li:
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        

        i += 1
        j -= 1
    elif s[i].lower() in vowel_li:
        j -= 1
    elif s[j].lower() in vowel_li:

        i += 1
    else:
        i += 1
        j -= 1    

s = ''.join(s)
print(s)