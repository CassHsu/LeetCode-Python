class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i, l, r = 0, 0, len(nums) - 1
        
        while i <= r:
            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            elif nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            else:
                i += 1