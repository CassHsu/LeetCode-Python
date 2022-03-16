class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalids = []
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack) == 0:
                    invalids.append(i)
                else:
                    stack.pop()
        
        count = 0
        for t in invalids + stack:
            target = t - count
            s = s[:target] + s[target + 1:]
            count += 1
            
        return s
