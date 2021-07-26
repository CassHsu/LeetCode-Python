class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mode = -1
        
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                if mode == 1:
                    return False
                else:
                    mode = 0
                    
            if nums[i - 1] > nums[i]:
                if mode  == 0:
                    return False
                else:
                    mode = 1
        return True
