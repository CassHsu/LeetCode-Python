class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        m = {}
        for i, k in enumerate(keyboard):
            m[k] = i
        
        ans = 0
        cur = 0
        for w in word:
            ans += abs(m[w] - cur)
            cur = m[w]
            
        return ans
