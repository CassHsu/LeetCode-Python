class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = len(nums) - 1
        l = 0
        ans = []
        
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans.append(nums[l]**2)
                l += 1
            else:
                ans.append(nums[r]**2)
                r -= 1
                
        return ans[::-1]
