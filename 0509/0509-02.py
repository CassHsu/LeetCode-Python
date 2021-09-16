class Solution:
    def fib(self, n: int) -> int:
        m = {}
        
        def dfs(x):
            nonlocal m
            if x < 2:
                return x
            
            v = dfs(x - 1) + dfs(x - 2)
            if x in m:
                return m[x]
            
            m[x] = v   
            return v
        
        return dfs(n)
