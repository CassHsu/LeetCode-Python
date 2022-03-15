class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        s = path.split('/')
        
        for c in s:
            if c == '..':
                if len(stack) > 0:
                    stack.pop()
            elif c != '' and c != '.':
                stack.append(c)
        
        return '/' + '/'.join(stack)
