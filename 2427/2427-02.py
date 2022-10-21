class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum([not (a % n or b % n) for n in range(1, min(a, b) + 1)])
