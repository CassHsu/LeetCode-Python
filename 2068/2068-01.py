from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        s = set(word1 + word2)
        
        for c in s:
            if abs(c1[c] - c2[c]) > 3:
                return False
            
        return True
