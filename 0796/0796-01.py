class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == '' and goal == '':
            return True
        
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return True
        
        g = goal
        for _ in range(len(s)):
            g = g[1:] + g[:1]
            if s == g:
                return True
        
        return False
