class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            n = nums.index(min(nums))
            nums[n] *= multiplier

        return nums
