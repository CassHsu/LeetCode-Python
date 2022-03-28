class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(start, end, t):
            if start > end:
                return -1
            
            mid = (start + end) // 2
            if nums[mid] == t:
                return mid
            
            if nums[mid] > t:
                return bin_search(start, mid - 1, t)
            
            if nums[mid] < t:
                return bin_search(mid + 1, end, t)
            
        return bin_search(0, len(nums) - 1, target)
