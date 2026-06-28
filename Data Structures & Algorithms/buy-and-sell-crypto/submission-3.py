class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        max_price = 0

        while right < len(prices):

            if (prices[right] < prices[left]):
                left = right

            max_price = max(max_price, prices[right] - prices[left])

            right += 1

        return max_price