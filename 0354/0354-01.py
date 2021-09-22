class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def lis(nums):
            dp = [1] * len(nums)
            
            for i in range(len(nums)):
                for j in range(i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            
            return max(dp)
        
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        return lis([e[1] for e in envelopes])
