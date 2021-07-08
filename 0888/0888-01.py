class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        ret = []
        sa = set(aliceSizes)
        sb = set(bobSizes)
        t = (sum(aliceSizes) - sum(bobSizes)) // 2
        
        for b in sb:
            if t + b in sa:
                ret.append(t + b)
                ret.append(b)
                return ret
        
        return ret
