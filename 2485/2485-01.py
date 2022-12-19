class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = []

        for i in range(1, n + 1):
            nums.append(i)

        for p in range(0, n + 1):
            if sum(nums[:p + 1]) == sum(nums[p:]):
                return p + 1

        return -1
