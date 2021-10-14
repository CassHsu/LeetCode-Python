class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        
        s = bin(n)[2:]
        
        if s.count('1') == 1:
            if len(s) % 2 == 1:
                return True
            
        return False
