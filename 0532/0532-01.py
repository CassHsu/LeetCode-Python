class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        r = 0
        c = Counter(nums)
        
        for n in c:
            if k > 0 and n + k in c:
                r += 1
            elif k == 0 and c[n] > 1:
                r += 1
                
        return r
