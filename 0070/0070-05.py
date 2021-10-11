class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        
        dp1 = 2
        dp2 = 3
        curr = 0
        
        for i in range(4, n+1):
            curr = dp1 + dp2
            dp1, dp2 = dp2, curr
        
        return curr
