class Solution:
    def reformat(self, s: str) -> str:
        a = []
        d = []
        
        for c in s:
            if c in ("1","2","3","4","5","6","7","8","9","0"):
                d.append(c)
            else:
                a.append(c)
                
        if abs(len(a) - len(d)) >= 2:
            return ""
        
        is_ad = True
        if len(d) > len(a):
            is_ad = False
        
        ans = ""
        while len(a) > 0 and len(d) > 0:
            if is_ad:
                ans += a.pop()
                ans += d.pop()
            else:
                ans += d.pop()
                ans += a.pop()
        
        if len(a) > 0:
            ans += a.pop()
        if len(d) > 0:
            ans += d.pop()
        
        return ans
