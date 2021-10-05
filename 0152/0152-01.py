class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [0] * len(nums)
        dp_min = [0] * len(nums)
        
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp_max[i] = max(max(nums[i] * dp_max[i - 1], nums[i]), nums[i] * dp_min[i - 1])
            dp_min[i] = min(min(nums[i] * dp_min[i - 1], nums[i]), nums[i] * dp_max[i - 1])
        
        return max(max(dp_max), max(dp_min))
