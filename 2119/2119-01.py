class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        r1 = str(num)[::-1]
        r2 = str(int(r1))[::-1]
        
        return int(r2) == num
