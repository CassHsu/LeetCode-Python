class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        
        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i == -1 or j == -1:
                return 0
            
            if text1[i] == text2[j]:
                cache[(i, j)] = dp(i-1, j-1) +1
            else:
                cache[(i, j)] = max(dp(i-1, j), dp(i, j-1))
                
            return cache[(i, j)]
        
        return dp(len(text1) - 1, len(text2) - 1)
