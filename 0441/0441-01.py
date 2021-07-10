class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 1:
            return 0
        count = 0
        
        for i in range(1, n + 1):
            count += i
            if n < count:
                return i - 1
            elif n == count:
                return i
