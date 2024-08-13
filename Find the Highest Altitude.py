gain = [-4,-3,-2,-1,4,3,2]

highest_altitude = gain[0]

sum_alt = 0

for i in range(len(gain)):
    sum_alt += gain[i]
    if sum_alt > highest_altitude:
        highest_altitude = sum_alt
      
if highest_altitude < 0:
    highest_altitude = 0  
print(highest_altitude)