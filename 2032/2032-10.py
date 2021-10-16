from collections import Counter

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = []
        for k, v in Counter(list(set(nums1)) + list(set(nums2)) + list(set(nums3))).items():
            if v >= 2:
                ans.append(k)
                
        return ans
