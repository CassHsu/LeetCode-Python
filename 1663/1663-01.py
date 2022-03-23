class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = [0 for _ in range(n)]
        a = ord('a')
        
        for i in range(n - 1, -1, -1):
            add = min(k - i, 26)
            ans[i] = chr(add + a - 1)
            k -= add
        
        return ''.join(ans)
