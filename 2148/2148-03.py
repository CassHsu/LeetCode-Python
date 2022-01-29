class Solution:
    def countElements(self, nums: List[int]) -> int:
        return len([n for n in nums if max(nums) > n > min(nums)])
