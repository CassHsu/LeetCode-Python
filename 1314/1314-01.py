class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # build 2D pre sum
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = mat[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

        ans = [[0] * n for _ in range(m)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                end_i = min(m, i+k)
                end_j = min(n, j+k)
                
                start_i = max(1, i-k)
                start_j = max(1, j-k)
                
                ans[i-1][j-1] = dp[end_i][end_j] - dp[start_i - 1][end_j] - dp[end_i][start_j-1] + dp[start_i-1][start_j-1]
                
        return ans
