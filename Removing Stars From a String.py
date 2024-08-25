s = "leet**cod*e"

res = ''
remove = 0

for char in s[::-1]:
    if char == "*":
        remove += 1

    else:
        if not remove:
            res += char
        else:
            remove -= 1

print(res)