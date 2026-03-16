def max_profit(prices):
    left = 0 # buy day
    right = 0 # sell day
    max_profit = 0
    
    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
            
        else:
            left = right
            
        right += 1
        
    return max_profit
