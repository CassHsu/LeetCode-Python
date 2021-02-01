class Solution:
    def searchInsert(self, nums, target) -> int:
        size = len(nums)
        if target > nums[size - 1]:
            return size
        if target <= nums[0]:
            return 0
        
        left, right = 0, size - 1
        while left != right:
            mid = (right + left) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left