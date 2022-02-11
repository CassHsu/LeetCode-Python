class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, total = 0, 0
        m = defaultdict(int)
        m[0] = 1
        
        for n in nums:
            total += n
            if total - k in m:
                count += m[total - k]
                
            m[total] += 1
        
        return count
