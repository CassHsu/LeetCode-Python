class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        counts = defaultdict(int)
        for w in words:
            counts[w] += 1
            
        def is_subseq(s, w):
            i = 0
            for c in w:
                i = s.find(c, i) + 1
                if not i:
                    return False
            return True
        
        res = 0
        for w in counts:
            if is_subseq(s, w):
                res += counts[w]
                
        return res
