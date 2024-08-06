str1 = "LEET"
str2 = "CODE"

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        q = a // b
        remainder = a - (b*q)

        return gcd(b, remainder)

length_str1 = len(str1)
length_str2 = len(str2)

length_str3 = gcd(length_str1, length_str2)

if str1[0] != str2[0]:
    print('')

if str1 + str2 == str2 + str1:
    print(str1[:length_str3])
else:
    print('')
