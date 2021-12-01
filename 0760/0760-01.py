class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        ans = []
        
        for i, n in enumerate(nums2):
            m[n] = i
            
        for n in nums1:
            ans.append(m[n])
        
        return ans
