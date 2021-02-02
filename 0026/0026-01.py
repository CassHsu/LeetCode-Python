class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        p = 0
        for i in range(1, len(nums)):
            if nums[p] != nums[i]:
                p += 1
                nums[p] = nums[i]
                
        return p + 1