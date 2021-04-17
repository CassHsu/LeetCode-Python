class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        for i in range(size//2, 0, -1):
            if size % i == 0:
                repeat = size // i
                substr = s[0:i]
                curr = ""
                for _ in range(repeat):
                    curr += substr[:]
                    
                if curr == s:
                    return True
                
        return False
