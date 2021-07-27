from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        
        num = c[s[0]]
        for k in c:
            if c[k] != num:
                return False
            
        return True
