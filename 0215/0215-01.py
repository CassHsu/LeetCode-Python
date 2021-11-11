from random import uniform

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def select(nums: List[int], k) -> int:
            pivot = int(uniform(0, len(nums)))
            l, r = [], []
            
            for i, n in enumerate(nums):
                if n <= nums[pivot] and i != pivot: l.append(n)
                if n > nums[pivot]: r.append(n)
            
            if k == len(l): return nums[pivot]
            elif k < len(l):
                return select(l, k)
            else:
                return select(r, k - len(l) - 1)
            
        return select(nums, k)
