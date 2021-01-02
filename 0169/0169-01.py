from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return cnt.most_common(1)[0][0]