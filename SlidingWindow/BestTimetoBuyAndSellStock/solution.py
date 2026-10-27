def maxProfit(prices: list[int]) -> int:
    min_price = max(prices)
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        if (price - min_price) > max_profit:
            max_profit = price - min_price
    return max_profit


prices = [10, 8, 7, 5, 2]

print(maxProfit(prices))
