class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l = list(range(1, n+1))
        x = k-1
        
        r = ""
        f = 1
        for i in range(2, n+1):
            f *= i
            
        for y in range(n, 0, -1):
            x = x % f
            f = 1
            for i in range(2, y):
                f *= i
                
            a = l[x//f]
            r += str(a)
            l.pop(x//f)
            
        return r
