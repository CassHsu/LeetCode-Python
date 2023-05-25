class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans = 0
        mx = max(nums)
        for i in range(k):
            ans += mx
            ans += i
        return ans
