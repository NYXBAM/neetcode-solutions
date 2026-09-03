def maxProfit(prices: list[int]) -> int:
    total = 0
    for n in range(len(prices) - 1):
        if prices[n] < prices[n + 1]:
            total += prices[n + 1] - prices[n]

    return total


prices = [7, 1, 5, 3, 6, 4]


print(maxProfit(prices))
