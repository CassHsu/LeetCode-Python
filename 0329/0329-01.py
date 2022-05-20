class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(i, j, prev_val):
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= prev_val:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = max(dfs(i+1, j, matrix[i][j]),
            dfs(i-1, j, matrix[i][j]),
            dfs(i, j-1, matrix[i][j]),
            dfs(i, j+1, matrix[i][j])) + 1
            
            return dp[i][j]

        res = -1
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, -1))
        return res
