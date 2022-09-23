class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        arr = s.split(' ')
        for i, w in enumerate(arr):
            res += w[::-1]
            if i != len(arr) - 1:
                res += " "
        return res
