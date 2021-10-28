class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        left = 0
        sums = 0
        
        for i in range(len(nums)):
            sums += nums[i]
            
            while sums >= target:
                ans = min(ans, i + 1 - left)
                sums -= nums[left]
                left += 1
                
        return ans if ans != float('inf') else 0
