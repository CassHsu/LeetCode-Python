class Solution:
    def repeatedCharacter(self, s: str) -> str:
        r = 0
        m = defaultdict(int)
        
        for i, c in enumerate(s):
            if m[c] > 0:
                r = i
                break
            m[c] += 1
        
        return s[r]
