class Solution:
    def isArmstrong(self, n: int) -> bool:
        return True if sum([pow(int(c), len(str(n))) for c in str(n)]) == n else False
