class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for s in strs:
            z = s.count('0')
            o = len(s) - z
            
            for i in range(n, o - 1, -1):
                for j in range(m, z - 1, -1):
                    dp[i][j] = max(1 + dp[i - o][j - z], dp[i][j])
                
        return dp[n][m]
