class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mx = amount + 1
        dp = [mx] * mx
        dp[0] = 0
        
        for a in range(1, mx):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != mx else -1
