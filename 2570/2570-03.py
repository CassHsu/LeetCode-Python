from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m = defaultdict(list)

        for i, v in nums1:
            m[i].append(v)

        for i, v in nums2:
            m[i].append(v)

        keys = sorted(list(m.keys()))
        
        return [[k, sum(m[k])] for k in keys]
