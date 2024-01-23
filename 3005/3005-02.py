class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        m = defaultdict(int)
        mx = 0
        count = 0

        for n in nums:
            f = m[n] + 1
            if f == mx:
                count += 1
            elif f > mx:
                mx = f
                count = 1

            m[n] = f

        return mx * count
