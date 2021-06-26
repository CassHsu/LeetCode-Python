def uniquePaths(m, n, cache):
    if m == 1 or n == 1:
        return 1
    
    if (m, n) in cache:
        return cache[(m, n)]
    
    cache[(m, n)] = uniquePaths(m - 1, n, cache) + uniquePaths(m, n - 1, cache)
    
    return cache[(m, n)]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return uniquePaths(m, n, {})
