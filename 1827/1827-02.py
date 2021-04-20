class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                diff = nums[i-1] - nums[i]
                diff += 1
                count += diff
                nums[i] += diff
        
        return count
