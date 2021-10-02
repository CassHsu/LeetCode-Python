class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        
        if size <= 3:
            return max(nums)
        

        def helper(dp):
            dp[1] = max(dp[0], dp[1])
            
            for n in range(2, len(dp)):
                dp[n] = max(dp[n - 1], dp[n] + dp[n - 2])
                
            return dp[-1]
        
        p1 = helper(nums[:size - 1])
        p2 = helper(nums[1:])
        
        return max(p1, p2)
