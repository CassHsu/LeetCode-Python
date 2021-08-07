from collections import defaultdict

class Solution:    
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:        
        m = defaultdict(lambda: 0)
        for w in s1.split():
            m[w] += 1
            
        for w in s2.split():
            m[w] += 1
        
        return [k for k, v in m.items() if v == 1]
