class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(1, len(s) - 1):
            if (s[i-1] != s[i] and s[i] != s[i+1] and s[i+1] != s[i-1]):
                count += 1
        
        return count
