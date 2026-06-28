class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0

        for i, price in enumerate(prices):
            if i == 0:
                continue

            if min(prices[:i]) < price and price - min(prices[:i]) > profit:
                profit = price - min(prices[:i])

        return profit