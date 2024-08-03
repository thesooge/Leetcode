text = "loonbalxballpoon"

ballon = "balloon"

ball_dict = {}



for i in text:
    if i in ball_dict:
        ball_dict[i] += 1
    else:
        ball_dict[i] = 1

free_str = ''
i = 0
counter = 0
while True:
    if ballon[i] not in text:
        break
    elif ball_dict[ballon[i]] > 0:
        free_str += ballon[i]
        ball_dict[ballon[i]] -= 1
        if free_str == ballon:
            counter += 1
            i = 0
            free_str = ''
        else:
            i += 1
    else:
        break

print(counter)    


