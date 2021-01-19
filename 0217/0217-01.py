class Solution:
    def containsDuplicate(self, nums) -> bool:
        m = {}
        for n in nums:
            v = m.get(n, 0)
            if v >= 1:
                return True
            m[n] = 1
            
        return False