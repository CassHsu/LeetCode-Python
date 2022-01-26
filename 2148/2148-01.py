class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        
        for i in range(1, len(nums) - 1):
            if min(nums[:i]) < nums[i] < max(nums[i+1:]):
                count += 1
        
        return count
