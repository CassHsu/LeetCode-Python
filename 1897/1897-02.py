from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        size = len(words)
        
        counts = Counter(''.join(words))
        for v in counts.values():
            if v % size != 0:
                return False
        
        return True
