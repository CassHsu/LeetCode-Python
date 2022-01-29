class Solution:
    def countElements(self, nums: List[int]) -> int:
        mx, mi = max(nums), min(nums)
        return len([n for n in nums if mx > n > mi])
