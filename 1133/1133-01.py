from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        singles = []
        for k, v in c.items():
            if v == 1:
                singles.append(k)
        
        return max(singles) if len(singles) > 0 else -1
