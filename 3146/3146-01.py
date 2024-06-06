class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        m = {}
        for i, c in enumerate(s):
            m[c] = i

        ans = 0
        for i, c in enumerate(t):
            ans += abs(i - m[c])

        return ans
