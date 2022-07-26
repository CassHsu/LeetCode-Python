class Solution:
    def repeatedCharacter(self, s: str) -> str:
        counts = defaultdict(int)
        r = s[0]
        for c in s:
            if counts[c] != 0:
                r = c
                break
            counts[c] += 1
            
        return r
