class Solution:
    def searchInsert(self, nums, target) -> int: 
        size = len(nums)
        if target > nums[size- 1]:
            return size
        
        res = 0
        for i, n in enumerate(nums):
            if n >= target:
                res = i
                break
        return res