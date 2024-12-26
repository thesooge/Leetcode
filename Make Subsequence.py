s = "abcde"
t = "a"

res = ""

i = 0
counter = 0
          

while True:
        if i == len(t):
            break
        elif s[i] == t[i]:
            res += s[i]
        i += 1
    

p = 0

for i in t:
    try:
        if i == res[p]:
            p += 1
            continue
        else:
            counter = len(t)
    except:
        if res != "":
            counter += 1
        continue


print(counter)