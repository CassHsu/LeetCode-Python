class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        
        m = n // 2
        if n % 2 != 0:
            m += 1

        for i in range(1, m):
            dp[i * 2] = dp[i]
            dp[(i * 2) + 1] = dp[i] + dp[i + 1]
        
        return max(dp)
