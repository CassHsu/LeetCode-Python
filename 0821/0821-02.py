class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        size = len(s)
        ans = []
        pos = []
        for i in range(size):
            if s[i] == c:
                pos.append(i)
                
        for i in range(size):
            n = size
            for p in pos:
                n = min(n, abs(i - p))
            
            ans.append(n)
            
        return ans
