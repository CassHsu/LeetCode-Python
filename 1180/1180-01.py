class Solution:
    def countLetters(self, s: str) -> int:
        count = 1
        dp = [0] * len(s)
        dp[0] = 1
        
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
                
            count += dp[i]
        
        return count
