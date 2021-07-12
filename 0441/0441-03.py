class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        
        while l <= r:
            m = (r + l) // 2
            curr = m * (m + 1) // 2
            
            if curr == n:
                return m
            if n < curr:
                r = m - 1
            else:
                l = m + 1
                
        return r
