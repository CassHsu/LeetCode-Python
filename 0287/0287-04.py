class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = nums[0]
        
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                ans = nums[i]
                break
                
        return ans
