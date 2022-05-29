class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        full = list(range(1, size + 1))
        
        xor = 0
        for n in nums:
            xor ^= n
            
        for f in full:
            xor ^= f
            
        return xor
