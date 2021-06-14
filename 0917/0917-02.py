class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        ret = []
        
        for c in s:
            if c.isalpha():
                ret.append(letters.pop())
            else:
                ret.append(c)
        
        return "".join(ret)
