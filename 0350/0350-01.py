class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []   
        c = Counter(nums2)
        
        for n in nums1:
            if n in c.keys() and c[n] > 0:
                res.append(n)
                c[n] -= 1
        
        return res