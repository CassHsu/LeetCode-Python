class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        size = len(nums)
        for i in range(0, size):
            for j in range(i + 1, size):
                if nums[i] + nums[j] < target:
                    count += 1

        return count
