class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        cs = Counter()
        
        for w in words2:
            cs |= Counter(w)
        
        for w in words1:
            if not cs - Counter(w):
                res.append(w)
                
        return res
