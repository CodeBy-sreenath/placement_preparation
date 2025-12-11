def max_profit(prices):
    max_profit=0
    min_price=float('inf')
    for price in prices:
        if price<min_price:
            min_price=price
        profit=price-min_price
        max_profit=max(max_profit,profit)
    return max_profit
prices=[7,1,5,3,6]
print(max_profit(prices))        