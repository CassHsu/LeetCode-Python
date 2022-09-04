class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        
        res = []
        
        def dfs(nn, num):
            if nn == 0:
                return res.append(num)
            
            d = num % 10
            next_set = set([d + k, d - k])
            
            for nx in next_set:
                if 0 <= nx < 10:
                    dfs(nn - 1, num * 10 + nx)
                    
        for num in range(1, 10):
            dfs(n - 1, num)
        
        return res
