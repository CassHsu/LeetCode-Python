class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        ans = nums[-1]
        i, j = 0, len(nums) - 1

        while i <= j:
            ans = min(ans, (nums[i] + nums[j]) / 2)
            i += 1
            j -= 1

        return ans
