class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 1
        
        for n in range(2, min(a, b) + 1):
            if a % n == 0 and b % n == 0:
                count += 1
        
        return count
