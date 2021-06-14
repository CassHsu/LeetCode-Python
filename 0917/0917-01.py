class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ret = []
        j = len(s) - 1
        for i, c in enumerate(s):
            if c.isalpha():
                while not s[j].isalpha():
                    j -= 1
                ret.append(s[j])
                j -= 1
            else:
                ret.append(c)
                
        return "".join(ret)
