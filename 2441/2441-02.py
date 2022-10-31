class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        m = defaultdict(int)
        
        for n in nums:
            m[n] += 1
        
        mx = -1
        for n in nums:
            if n > 0 and m[-n] > 0 and n > mx:
                mx = n
        
        return mx
