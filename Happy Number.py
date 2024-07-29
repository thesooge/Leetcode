n = 7


if n == 7 or n == 1:
    print(True) 
while n > 9:

    
    new_n = 0
    for i in str(n):
        new_n += int(i) ** 2
        n = new_n

    
print(n)    