class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [[0] * 2 for _ in range(size)]
        
        if nums[0] > 0:
            dp[0][0] = 1
            
        if nums[0] < 0:
            dp[0][1] = 1
            
        ans = dp[0][0]
        
        for i in range(1, size):
            curr = nums[i]
            
            if curr > 0:
                dp[i][0] = dp[i-1][0] + 1
                
                if dp[i-1][1] > 0:
                    dp[i][1] = max(dp[i][1], dp[i-1][1] + 1)
                
            if curr < 0:
                dp[i][1] = dp[i - 1][0] + 1
                
                if dp[i-1][1] > 0:
                    dp[i][0] = max(dp[i][0], dp[i-1][1] + 1)
                
            ans = max(ans, dp[i][0])
        
        return ans
