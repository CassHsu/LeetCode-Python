class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        
        prev = '0'
        curr = s[0]
        
        for i in range(2, n + 1):
            prev = curr
            curr = s[i - 1]
            
            if curr != '0':
                dp[i] += dp[i - 1]
                
            if prev == '1' or (prev == '2' and curr <= '6'):
                dp[i] += dp[i - 2]
                
        return dp[-1]
