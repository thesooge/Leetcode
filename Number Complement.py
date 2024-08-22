num = 1
tmp = ''

str_bin = bin(num)[2:]

def binaryToDecimal(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)

for i in str_bin:
    if i == '1':
        tmp += '0'
    else:
        tmp += '1' 

print(binaryToDecimal(int(tmp)))           