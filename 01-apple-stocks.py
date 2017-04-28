def get_max_profits(stock_prices):
    
    if len(stock_prices) < 2:
        raise IndexError('Profit requires at least two prices')
    
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    
    for index, price in enumerate(stock_prices):
         if index == 0:
            continue
        max_profit = max(potential_max, max_profit)
        min_price = min(min_price, price)
        
    return max_profit


print get_max_profits([10, 7, 5, 4, 3, 2])

