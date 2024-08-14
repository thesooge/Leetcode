s = "a good   example"
new_str = ''


s = s[::-1]


s = (s.split(' '))  
for word in s:
    if word == '':
        continue
    else:
        new_str += word[::-1] + ' '   

new_str = new_str.removesuffix(' ')
print(new_str)
    