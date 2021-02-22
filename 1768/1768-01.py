class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        i = 0
        ret = ""
        
        while w1 > 0 and w2 > 0:
            ret += word1[i]
            ret += word2[i]
            i += 1
            w1 -= 1
            w2 -= 1
        
        if w1 > 0:
            ret += word1[i:]
        else:
            ret += word2[i:]
            
        return ret
