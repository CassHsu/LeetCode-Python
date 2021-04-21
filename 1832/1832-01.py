class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        
        m = {}
        for alphabet in "abcdefghijklmnopqrstuvwxyz":
            m[alphabet] = 0
            
        for s in sentence:
            m[s] += 1
            
        for _, v in m.items():
            if v == 0:
                return False
            
        return True
