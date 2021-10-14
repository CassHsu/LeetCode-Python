class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        
        def helper(r, c):
            if r == 1 or c == 1:
                return 1
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            cache[(r, c)] = helper(r - 1, c) + helper(r, c - 1)
            return cache[(r, c)]
        
        return helper(m, n)
