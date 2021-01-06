class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        lastIdxs = {}
        ans = -1
        
        for i, c in enumerate(s):
            if c not in lastIdxs:
                lastIdxs[c] = i
            else:
                ans = max(ans, i - lastIdxs[c] -1)
        
        return ans