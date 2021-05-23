class Solution:
    def numTrees(self, n: int) -> int:
        cache = [0] * (n + 1)
        cache[0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                cache[i]  += cache[j - 1] * cache[i - j]
            
        return cache[n]
