class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = [False] * need
        all_1 = need - 1
        key = 0
        
        for i in range(len(s)):
            key = ((key << 1) & all_1) | (int(s[i]))
            
            if i >= k - 1 and got[key] is False:
                got[key] = True
                need -= 1
                if need == 0:
                    return True
                
        return False
