class Solution:
    def isValid(self, s: str) -> bool:
        m = defaultdict(str)
        
        m['('] = ')'
        m['['] = ']'
        m['{'] = '}'
        
        stack = []
        
        for c in s:
            if stack and m[stack[-1]] == c:
                stack.pop()
            else:
                stack.append(c)
                
        return not stack
