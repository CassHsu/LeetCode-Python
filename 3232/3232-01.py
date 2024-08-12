class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s, d = 0, 0

        for n in nums:
            if len(str(n)) == 1:
                s += n
            else:
                d += n

        return s != d
