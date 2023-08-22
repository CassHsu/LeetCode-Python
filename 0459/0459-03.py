class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False

        ss = s + s
        ss = ss[1: -1]

        return s in ss
