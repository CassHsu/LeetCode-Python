class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target or nums[l] == target or nums[r] == target:
                return True
            
            if nums[l] < nums[r]:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            elif nums[l] >= nums[r] :
                r -= 1
                
        return False
