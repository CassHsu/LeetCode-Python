class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s = bin(n)
        return s.startswith('0b1') and all(c == '0' for c in s[3:])