class Solution:
    def shift(self, c, x):
        return chr(ord(c) + x)
    
    def replaceDigits(self, s: str) -> str:
        ret = ""
        for i, v in enumerate(s):
            if i % 2 != 0:
                ret += self.shift(s[i-1], int(s[i]))
            else:
                ret += v
        return ret
