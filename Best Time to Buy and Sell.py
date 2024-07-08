prices = [7,1,5,3,6,4]


profit = 0

minimum = prices[0]

for i in range(len(prices)):
    minimum = min(prices[i], minimum)
    profit = max(profit, prices[i]- minimum)

print(profit)
