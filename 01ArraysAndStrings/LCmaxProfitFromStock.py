class Solution:
    def maxProfit(self, prices):
        minPrice = sys.maxsize
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit