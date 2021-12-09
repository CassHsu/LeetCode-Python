class Solution:
    def isArmstrong(self, n: int) -> bool:
        sn = str(n)
        size = len(sn)
        return True if sum([pow(int(c), size) for c in sn]) == n else False
