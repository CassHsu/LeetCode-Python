class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        r = 0
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        
        for key, value in m.items():
            if k > 0 and key + k in m:
                r += 1
            elif k == 0 and value > 1:
                r += 1
                
        return r
