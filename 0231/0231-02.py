class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        k = 1
        for x in range(31):
            if k == n:
                return True
            k *= 2
        return False