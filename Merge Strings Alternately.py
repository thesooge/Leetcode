word1 = "ab"
word2 = "pqrs"
res_str = ""

length = min(len(word1), len(word2))
i = 0
j = 0
while True:
    if i < length and j < length:
        res_str += word1[i]
        res_str += word2[j]
        i += 1
        j += 1
    elif i < len(word1) and j >= len(word2):

        res_str += word1[i]
        i += 1    
    elif j < len(word2) and i >= len(word1):

        res_str += word2[j]
        j += 1    
    else:
        break
        

print(res_str)        