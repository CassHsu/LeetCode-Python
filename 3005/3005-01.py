class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        mx = max(c.values())
        count = 0

        for v in c.values():
            if v == mx:
                count += v

        return count
