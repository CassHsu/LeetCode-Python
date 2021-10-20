class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}
        
        def dp(m):
            if m in cache:
                return cache[m]
            
            if n == 1:
                return 1
            
            res = float('-inf')
            for v in range(1, m):
                res = max(res, dp(v) * (m - v), v * (m - v))
                
            cache[m] = res
            return res
        
        return dp(n)
