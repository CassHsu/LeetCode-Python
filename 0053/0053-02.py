class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        ans = dp[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            if dp[i] > ans:
                ans = dp[i]
        
        return ans
