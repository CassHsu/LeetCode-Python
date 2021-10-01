class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = ""
        count = 1
        ans = ""
        
        for c in s:
            if c == prev:
                count += 1
            else:
                count = 1
                
            if count < 3:
                ans += c
                
            prev = c
            
        return ans
