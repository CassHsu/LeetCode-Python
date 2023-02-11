class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            ans.extend([int(c) for c in str(n)])

        return ans
