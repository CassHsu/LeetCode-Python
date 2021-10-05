class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        m = {}
        count = 0
        start, end = 0, 0
        
        for end, c in enumerate(s):
            if c in m:
                start = max(m[c], start)
                
            count = max(count, end - start + 1)
            m[c] = end + 1
        
        return count
