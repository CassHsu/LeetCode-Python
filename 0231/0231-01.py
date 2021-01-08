class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for x in range(31):
            p = 2 ** x
            if n == p:
                return True
            
        return False