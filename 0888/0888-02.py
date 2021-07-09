class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sa = set(aliceSizes)
        sb = set(bobSizes)
        t = (sum(bobSizes) - sum(aliceSizes)) // 2
        
        return [[b - t, b] for b in sb if (b - t) in sa][0]
