class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        
        cs = Counter(s)
        
        h = [(-f, k*f) for k,f in cs.items()]
        
        heapq.heapify(h)
        res = ''
        
        while len(h) > 0:
            f, k = heapq.heappop(h)
            res += k
            
        return res
