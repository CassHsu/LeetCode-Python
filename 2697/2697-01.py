class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l, r = 0, len(s) - 1
        d = []
        
        while l < r:
            if s[l] != s[r]:
                if s[l] > s[r]:
                    d.append((l, r))
                else:
                    d.append((r, l))
            l += 1
            r -= 1

        res = [c for c in s]
        for l, r in d:
            res[l] = s[r]

        return ''.join(res)
