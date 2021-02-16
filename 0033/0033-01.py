class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = math.floor((start + end) / 2)
            
            if nums[mid] == target:
                return mid
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end

            if nums[start] < target < nums[mid]:
                end = mid - 1
                
            elif nums[mid] < target < nums[end]:
                start = mid + 1
                
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
            
        return -1