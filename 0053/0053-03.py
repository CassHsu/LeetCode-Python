class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        dp_0 = nums[0]
        dp_1 = 0
        ans = dp_0
        
        for i in range(1, len(nums)):
            dp_1 = max(nums[i], nums[i] + dp_0)
            dp_0 = dp_1
            ans = max(ans, dp_1)
        
        return ans
