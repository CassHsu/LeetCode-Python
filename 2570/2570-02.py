class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m = defaultdict(list)

        for i, v in nums1:
            m[i].append(v)

        for i, v in nums2:
            m[i].append(v)

        keys = list(m.keys())
        keys.sort()

        ans = []
        for k in keys:
            ans.append((k, sum(m[k])))

        return ans
