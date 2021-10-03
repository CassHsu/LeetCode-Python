class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if far <= i:
                return False
        
        return far >= len(nums) - 1
