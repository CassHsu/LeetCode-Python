class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        
        for i, n1 in enumerate(nums):
            for j in range(i):
                if n1 > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
