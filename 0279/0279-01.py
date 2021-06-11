cache = {}

def numSquares(n):
    if n == 0:
        return 0
    if n in cache:
        return cache[n]
    
    i = 1
    k = i * i
    ans = None
    
    while k <= n:
        res = 1 + numSquares(n - k)
        if ans == None:
            ans = res
        else:
            ans = min(ans, res)
        
        i += 1
        k = i * i
    cache[n] = ans
    return ans

class Solution:
    def numSquares(self, n: int) -> int:
        return numSquares(n)
