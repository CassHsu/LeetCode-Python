class Solution(object):
    def deleteAndEarn(self, nums):
        nums.sort()
        
        n = nums[-1]        
        dp = [0] * (n + 1)
        for k in nums:
            dp[k] += k
            
        # Part from House Robber
        p1 = 0
        p2 = 0
        for i in range(n+1):
            ans = max(p2, p1 + dp[i])
            p1 = p2
            p2 = ans
            
        return ans
