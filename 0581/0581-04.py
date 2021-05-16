class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums = sorted(nums)
        check = [a == b for a, b in zip(nums, snums)]
        
        if all(check):
            return 0
        
        l = check.index(False)
        r = len(nums) - check[::-1].index(False)
        
        return r - l
