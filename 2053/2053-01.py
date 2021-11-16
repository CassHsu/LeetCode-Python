from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        
        for i, a in enumerate(arr):
            if c[a] == 1:
                k -= 1
                if k == 0:
                    return a
            
        return ""
