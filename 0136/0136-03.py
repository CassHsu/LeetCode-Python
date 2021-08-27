from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        ans = nums[0]
        
        for k, v in c.items():
            if v == 1:
                ans = k
                break
        
        return ans
