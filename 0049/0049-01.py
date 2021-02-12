class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            k = ''.join(sorted(s))
            if k in m:
                m.get(k).append(s)
            else:
                m[k] = [s]
        return m.values()