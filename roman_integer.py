val_sympbol = {"I" : 1 ,"V" : 5 ,"X" : 10 , "L" : 50 , "C" : 100 , "D" : 500 , "M" : 1000}

# print(val_sympbol["I"] + val_sympbol["V"])
def romanToint(s):
    counter = 1
    last_num = 0
    valid_value = ["I", "X", "C"]
    for i in s:
        try:
            if val_sympbol[i] < val_sympbol[s[counter]]:
                last_num -= val_sympbol[i]

            else:
                last_num += val_sympbol[i]
            counter += 1
        except:
            last_num += val_sympbol[i]
            continue    
    
    print(last_num)
romanToint("MCMXCIV")        
