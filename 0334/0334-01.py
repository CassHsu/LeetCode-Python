class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:        
        m1 = m2 = float('inf')
        
        for n in nums:
            if m1 < m2 < n:
                return True
            elif n < m1:
                m1 = n
            elif m1 < n < m2:
                m2 = n
            
        return False
