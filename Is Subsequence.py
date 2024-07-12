s = "axc"

t = "ahbgdc"

s_pointer = 0
t_pointer = 0
condition = False

while True:
    if s_pointer >= len(s):
        condition = True
        break
    elif t_pointer >= len(t):
        break    

    elif s[s_pointer] == t[t_pointer]:
        s_pointer += 1
        t_pointer += 1
    else: 
        t_pointer += 1

print(condition)
