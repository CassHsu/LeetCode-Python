class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0

        while len(g) > 0 and len(s) > 0:
            if s[0] >= g[0]:
                count += 1
                g = g[1:]

            s = s[1:] 

        return count
