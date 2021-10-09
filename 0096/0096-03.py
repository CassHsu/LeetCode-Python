class Solution:
    def numTrees(self, n: int) -> int:
        cache = {}
        
        def dfs(m):
            if m == 0:
                return 1
            
            if m in cache:
                return cache[m]
            
            ans = 0
            for i in range(1, m+1):
                ans += dfs(i-1) * dfs(m - i)

            cache[m] = ans
            return ans
            
        return dfs(n)
