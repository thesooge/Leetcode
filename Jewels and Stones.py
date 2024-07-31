jewels = "aA"
stones = "aAAbbbb"
count = 0

for i in stones:
    if i in jewels:
        count += 1

print(count)       