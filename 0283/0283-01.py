class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != p:
                    nums[p], nums[i] = nums[i], nums[p]
                p += 1