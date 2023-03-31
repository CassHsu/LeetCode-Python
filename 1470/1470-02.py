class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        size = len(nums)
        ans = [0 for i in range(size)]

        j, k = 0, n
        for i in range(size):
            if i % 2 == 0:
                ans[i] = nums[j]
                j += 1
            else:
                ans[i] = nums[k]
                k += 1

        return ans
