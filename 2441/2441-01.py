class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        m = defaultdict(int)
        
        for n in nums:
            m[n] += 1
        
        pn = []
        for n in nums:
            if n > 0 and m[-n] > 0:
                pn.append(n)
        
        return max(pn) if len(pn) > 0 else -1
