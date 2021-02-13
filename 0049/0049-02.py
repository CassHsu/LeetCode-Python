class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)
        for s in strs:
            m["".join(sorted(s))].append(s)
        return m.values()
