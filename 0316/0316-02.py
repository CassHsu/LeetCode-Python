class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        
        for c in s:
            if c in stack:
                count[c] -= 1
                continue
                
            while len(stack) > 0 and stack[-1] > c and count[stack[-1]] > 0:
                stack.pop()
                
            count[c] -= 1
            stack.append(c) 
            
        return ''.join(stack)
