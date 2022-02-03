class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        m = {}
        
        for n1 in nums1:
            for n2 in nums2:
                m[n1 + n2] = m.get(n1 + n2, 0) + 1
                
        for n3 in nums3:
            for n4 in nums4:
                count += m.get(-(n3 + n4), 0)
        
        return count
