class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack) == 0:
                    res.append(i)
                else:
                    stack.pop(-1)
                    
        count = 0
        for i in res + stack:
            idx = i - count
            s = s[:idx] + s[idx + 1:]
            count += 1
            
        return s
