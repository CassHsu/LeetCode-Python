class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        w1, w2, wt = "", "", ""
        
        for w in firstWord:
            w1 += str(ord(w) - 97)
            
        for w in secondWord:
            w2 += str(ord(w) - 97)
            
        for w in targetWord:
            wt += str(ord(w) - 97)
            
        return int(w1) + int(w2) == int(wt)
