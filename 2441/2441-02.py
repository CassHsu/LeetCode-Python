class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        m = defaultdict(int)
        
        for n in nums:
            m[n] += 1

            if m[-n]:
                res = max(res, abs(n))
        
        return res
