from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = Counter(s)
        ct = Counter(t)
        
        for k, v in ct.items():
            if cs[k] == None or cs[k] != v:
                return k
            
        return None
