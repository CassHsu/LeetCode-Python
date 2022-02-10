class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        
        if k > 0:
            for key in m.keys():
                if key + k in m:
                    count += 1
        if k == 0:
            for val in m.values():
                if val > 1:
                    count += 1
                
        return count
