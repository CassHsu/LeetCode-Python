# TLE
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        
        for i in range(len(nums)):
            sub_sum = 0 
            for j in range(i, len(nums)):
                sub_sum += nums[j]
                
                if sub_sum > ans:
                    ans = sub_sum;
                    
        return ans
