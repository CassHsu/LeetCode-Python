class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        mx, up, dn = 1, 1, 1

        for i in range(1, len(nums)):
            up = up + 1 if nums[i] > nums[i - 1] else 1  
            dn = dn + 1  if nums[i] < nums[i - 1] else 1
            mx = max(mx, up, dn)

        return mx
