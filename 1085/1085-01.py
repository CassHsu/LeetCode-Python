class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minimal = min(nums)

        ans = 0
        for n in str(minimal):
            ans += int(n)

        return 1 if ans % 2 == 0 else 0
