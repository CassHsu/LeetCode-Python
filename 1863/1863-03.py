class Solution:
    def __init__(self):
        self.ans = 0
        
    def xor_sum(self, nums, i, xor):
        if i >= len(nums):
            self.ans += xor
        else:
            self.xor_sum(nums, i + 1, nums[i] ^ xor)
            self.xor_sum(nums, i + 1, xor)
    
    def subsetXORSum(self, nums: List[int]) -> int:
        self.xor_sum(nums, 0, 0)
        return self.ans
