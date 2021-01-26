class Solution:
    def maxProfit(self, prices):
        res = 0
        size = len(prices)
        for i in range(1, size):
            pf = prices[i] - prices[i - 1]
            if pf > 0:
                res += pf
        return res