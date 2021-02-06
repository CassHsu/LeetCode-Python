class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        isConti = True
        stop = 1
        while isConti:
            isConti= False
            for i in range(len(nums) - stop):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    isConti = True
            stop += 1