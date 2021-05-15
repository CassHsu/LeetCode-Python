class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        r = 0
        l = len(nums)
        
        snums = sorted(nums.copy())
        
        for i in range(len(nums)):
            if nums[i] != snums[i]:
                r = max(r, i)
                l = min(l, i)
        
        return r - l + 1 if r - l >= 0 else 0
