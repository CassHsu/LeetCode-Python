class Solution:
    def concatenatedBinary(self, n: int) -> int:
        m = 10**9 + 7
        c = ''.join(bin(i)[2:] for i in range(n + 1))
        return int(c, 2) % m
