class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = defaultdict(list)
        for i, c in enumerate(s):
            m[c].append(i)
            
        counts = [arr[0] for arr in m.values() if len(arr) == 1]
        if len(counts) >= 1:
            return counts[0]
        else:
            return -1
