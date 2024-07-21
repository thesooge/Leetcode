
ransomNote = "aaabb"

magazine = "aab"

free_dict = {}

for i in magazine:
    if i in free_dict:
        free_dict[i] += 1
    else:
        free_dict[i] = 1

for j in ransomNote:
    if j in free_dict and free_dict[j] != 0:
        free_dict[j] -= 1
    else:
        print(False)    

print(True)
print(free_dict)