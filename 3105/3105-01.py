class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_i, max_d = 1, 1
        count_i, count_d = 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count_i += 1
            else:
                count_i = 1

            if nums[i] < nums[i - 1]:
                count_d += 1
            else:
                count_d = 1

            if count_i > max_i:
                max_i = count_i
            if count_d > max_d:
                max_d = count_d

        return max(max_i, max_d)
