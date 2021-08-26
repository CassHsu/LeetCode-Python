class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            find = target - n
            
            if find in m:
                return [m[find], i]
            
            m[n] = i
            
        return [-1, -1]
