class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        far = 0
        jump = 0
        
        for i in range(len(nums) - 1):
            far = max(nums[i] + i, far)
            
            if end == i:
                jump += 1
                end = far
                
        return jump
