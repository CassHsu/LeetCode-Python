class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        p = self.findPattern(pattern)
        for w in words:
            if p == self.findPattern(w):
                res.append(w)
        return res
    
    def findPattern(self, pattern):
        pm = {}
        code = ""
        i = 0
        for p in pattern:
            if pm.get(p) == None:
                pm[p] = i
                i += 1
            code += str(pm[p])
        return code
