class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mx = 0
        for st in strs:
            try:
                v = int(st)
            except:
                v = len(st)
            finally:
                mx = max(mx, v)

        return mx
