def max_profit(prices):
    if len(prices) < 2:
        return -1
    
    buy_day = 0
    sell_day = 0
    max_profit = 0
    min_price = prices[0]
    
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            sell_day = i
    
    if max_profit == 0:
        return -1
    
    print(f'Buy on day {buy_day+1} at price {prices[buy_day]}')
    print(f'Sell on day {sell_day+1} at price {prices[sell_day]}')
    print(f'Max profit: {max_profit}')
    return max_profit

assert max_profit([100, 180, 260, 310, 40, 535, 695]) == 655
assert max_profit([100, 90, 80, 70, 60]) == -1
assert max_profit([100, 200, 300, 400, 500]) == 400
assert max_profit([500, 400, 300, 200, 100]) == -1
assert max_profit([100, 200, 300, 200, 100]) == 200