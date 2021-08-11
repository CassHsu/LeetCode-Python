class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        
        def xor_sum(i, xor):
            nonlocal ans
            nonlocal nums
            if i >= len(nums):
                ans += xor
            else:
                xor_sum(i + 1, nums[i] ^ xor)
                xor_sum(i + 1, xor)
                
        xor_sum(0, 0)
        return ans
