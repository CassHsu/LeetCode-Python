class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        mx = max(nums)
        mi = min(nums)
        
        for i in range(1, len(nums) - 1):
            if mi < nums[i] < mx:
                count += 1
        
        return count
