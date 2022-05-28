class Solution:
    def numberOfSteps(self, num: int) -> int:
        b = bin(num)[2:]
        ones = b.count('1')
        count = len(b)
        return ones + count - 1
