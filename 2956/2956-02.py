class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = 0, 0

        for x in nums1:
            if x in nums2:
                count1 += 1

        for x in nums2:
            if x in nums1:
                count2 += 1

        return count1, count2
