class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        ord_num1 = sorted(nums1)
        ord_num2 = sorted(nums2)

        return ord_num2[0] - ord_num1[0]
