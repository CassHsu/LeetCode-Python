class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        s, t = len(stamp), len(target)
        res = []
        
        cover = set()
        for i in range(s):
            for j in range(s - i):
                cover.add('?' * i + stamp[i: s - j] + '?' * j)
                
        d = '?' * t
        p = t - s + 1
        
        while target != d:
            found = False
            for i in range(p, -1, -1):
                if target[i: i + s] in cover:
                    target = target[:i] + '?' * s + target[i + s:]
                    res.append(i)
                    found = True
            
            if not found:
                return []
            
        return res[::-1]
