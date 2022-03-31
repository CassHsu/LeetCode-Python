class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        
        a1 = [n for n in s1 - s2]
        a2 = [n for n in s2 - s1]
        return [a1, a2]
