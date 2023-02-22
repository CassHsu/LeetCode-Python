from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        def fn(v):
            return v[0]

        m = defaultdict(list)

        for i, v in nums1:
            m[i].append(v)

        for i, v in nums2:
            m[i].append(v)

        ans = []
        for k, v in m.items():
            ans.append([k, sum(m[k])])
        ans.sort(key=fn)

        return ans
