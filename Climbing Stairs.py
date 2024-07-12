
my_dict = {0:0, 1:1, 2:2, 3:3}

def s(n):
    a, b = 0, 1
    i = 0
     
    while i< n:
        a, b = b, a + b
        i += 1 

    return b
print(s(5))