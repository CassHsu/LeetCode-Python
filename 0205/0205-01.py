class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ms = {}
        mt = {}
        i = 0
        for cs, ct in zip(s, t):
            if cs not in ms:
                ms[cs] = i
            if ct not in mt:
                mt[ct] = i
                
            if ms[cs] != mt[ct]:
                return False
            i += 1
        
        return True
