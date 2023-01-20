class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digits = ''
        for n in nums:
            digits += str(n)

        digit_sum = 0

        for d in digits:
            digit_sum += int(d)

        return abs(element_sum - digit_sum)
