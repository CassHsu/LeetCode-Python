class Solution:
    def replaceDigits(self, s: str) -> str:
        return "".join([chr(ord(s[i-1]) + int(v)) if i % 2 != 0 else v for i, v in enumerate(s)])
