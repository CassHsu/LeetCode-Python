class Solution:
    def greatestLetter(self, s: str) -> str:
        counts = collections.Counter(s)
        uppers = [c for c in counts.keys() if c.isupper()]
        uppers.sort()
        
        greatest = ''
        for c in uppers[::-1]:
            if c.lower() in counts.keys():
                greatest = c
                break
        
        return greatest
