class Solution:
    def sortSentence(self, s: str) -> str:
        ss = s.split(' ')
        
        ret = [s for s in ss]
        for w in ss:
            i = int(w[-1])
            ret[i-1] = w[0:-1]
            
        return ' '.join(ret)
