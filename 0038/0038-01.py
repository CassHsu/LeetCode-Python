class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        cs = self.countAndSay(n - 1)
        num = 0
        init = cs[0]
        res = ""
        
        for c in cs:
            if c == init:
                num += 1
            else:
                res += str(num) + init
                num = 1
                init = c
        res += str(num) + init
        return res