class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        m = defaultdict(int)
        c = Counter(nums)
        
        for n in nums:
            if not c[n]:
                continue
                
            if m[n - 1] > 0:
                m[n - 1] -= 1
                m[n] += 1
                c[n] -= 1
            else:
                if not c[n + 1] or not c[n + 2]:
                    return False
                
                c[n] -= 1
                c[n + 1] -= 1
                c[n + 2] -= 1
                m[n + 2] += 1
                
        return True
