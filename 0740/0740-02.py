from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        prev = None
        avoid = using = 0
        
        for n in sorted(counts):
            if n - 1 != prev:
                avoid, using = max(avoid, using), n * counts[n] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), n * counts[n] + avoid
                
            prev = n
            
        return max(avoid, using)
