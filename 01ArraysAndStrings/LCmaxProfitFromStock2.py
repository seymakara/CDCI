class Solution:
    def maxProfit(self, prices):
        total = 0 
        for i in range(len(prices)-1): # it should stop looping at the second to last item.
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
        return total