class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        dp = [0] * size
        dp[0] = nums[0]
        
        for i in range(1, size - 1):
            if dp[i - 1] < i:
                return False
            
            dp[i] = max(i + nums[i], dp[i - 1])
            
            if dp[i] >= size - 1:
                return True
        
        return dp[size - 2] >= size - 1
