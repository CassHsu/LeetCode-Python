class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        res = ''

        i = 0
        while i < w1 or i < w2:
            if i < w1:
                res += word1[i]
            if i < w2:
                res += word2[i]
            i += 1
        
        return res
