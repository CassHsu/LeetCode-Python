class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or haystack == needle:
            return 0
        
        hSize = len(haystack)
        nSize = len(needle)
        p = 0
        while p <= hSize - nSize:
            if haystack[p: p + nSize] == needle:
                return p
            else:
                p += 1
        return -1