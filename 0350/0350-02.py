class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        m = DefaultDict(int)
        
        for n in nums1:
            m[n] += 1
            
        for n in nums2:
            if n in m.keys() and m[n] > 0:
                res.append(n)
                m[n] -= 1
        
        return res
