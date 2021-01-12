class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        p = 1
        for i in range(31):
            if p == n:
                return True
            p *= 3
        
        return False