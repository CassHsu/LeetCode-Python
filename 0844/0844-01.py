class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def buildit(st):
            r = []
            for c in st:
                if c == '#':
                    if len(r) > 0:
                        r.pop()
                else:
                    r.append(c)
                    
            return ''.join(r)
        
        return buildit(s) == buildit(t)
