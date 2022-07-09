class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen = set()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        w = ''
        for k in key:
            if k != ' ' and k not in seen:
                w += k
                seen.add(k)
        
        m = {}
        for i, c in enumerate(w):
            m[c] = alphabet[i]
            
        ans = ''
        for i, c in enumerate(message):
            if c == ' ':
                ans += ' '
                continue
                
            ans += m[c]
                
        return ans
