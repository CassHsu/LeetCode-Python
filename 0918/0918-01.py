class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def max_subarr(arr):
            max_sum = arr[0]
            cur_sum = 0
            
            for a in arr:
                if cur_sum < 0:
                    cur_sum = 0
                
                cur_sum += a
                max_sum = max(cur_sum, max_sum)
                
            return max_sum
        
        ans_kandane = max_subarr(nums)
        total = 0
        
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = -nums[i]
            
        ans_wrap = max_subarr(nums) + total
        
        if(ans_wrap == 0):
            return ans_kandane
        
        return max(ans_kandane, ans_wrap)
