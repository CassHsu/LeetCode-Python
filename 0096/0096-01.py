class Solution:
    def numTrees(self, n: int) -> int:
        return self.num_tree(n, {})
    
    def num_tree(self, n, cache):
        if n == 0:
            return 1
        
        if n in cache:
            return cache[n]
        
        ans = 0
        for i in range(1, n + 1):
            ans += self.num_tree(i - 1, cache) * self.num_tree(n - i, cache)
        
        cache[n] = ans
        return ans
