class Solution:
    def countLetters(self, s: str) -> int:
        count = 1
        dp = 1
        
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                dp += 1
            else:
                dp = 1
                
            count += dp
        
        return count
