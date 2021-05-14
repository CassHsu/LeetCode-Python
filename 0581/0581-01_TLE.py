class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        r = 0
        l = len(nums)
        
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    r = max(r, j)
                    l = min(l, i)
                    
        return r - l + 1 if r - l > 0 else 0
