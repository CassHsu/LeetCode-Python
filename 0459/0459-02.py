class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        for i in range(1, size//2 + 1):
            if size % i == 0:
                repeat = size // i
                substr = s[:i]
                curr = ""
                
                for _ in range(repeat):
                    curr += substr
                    
                if curr == s:
                    return True
                
        return False
