prices = [7,6,4,3,1]

left = 0 # buy
right = 1 # sell

total_profit = 0


while right < len(prices):
    if prices[left] < prices[right]:
        total_profit += prices[right] - prices[left]
    
    left = right    
    right += 1        


print(total_profit)
