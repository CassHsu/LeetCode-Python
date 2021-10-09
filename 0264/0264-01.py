class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def ugly(N):
            cache = [None] * (N+1)
            cache[1] = 1
            
            min2i = min3i = min5i = 1
            
            for i in range(2, N+1):
                min2 = cache[min2i] * 2
                min3 = cache[min3i] * 3
                min5 = cache[min5i] * 5
                
                cache[i] = min(min2, min3, min5)
                
                if min2 == cache[i]:
                    min2i += 1
                if min3 == cache[i]:
                    min3i += 1
                if min5 == cache[i]:
                    min5i += 1
                    
            return cache[N]
            
        return ugly(n)
