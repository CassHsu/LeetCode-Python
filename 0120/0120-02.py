class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = list(triangle[-1])
        
        for i in range(len(triangle) - 2, -1, -1):
            for j, n in enumerate(triangle[i]):
                dp[j] = n + min(dp[j], dp[j+1])
        
        return dp[0]
