class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        dp = [0] * len(prices)
        
        for i in range(1, len(prices)):
            dp[i] = dp[i-1] + max(0, prices[i] - prices[i-1])
            
        return dp[-1]
