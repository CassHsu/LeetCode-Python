class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        targets = [i for i, n in enumerate(nums) if n == target]
        
        if len(targets) == 0:
            return [-1, -1]
        if len(targets) == 1:
            return [targets[0], targets[0]]
        if len(targets) == 2:
            return targets
        else:
            return [targets[0], targets[-1]]
