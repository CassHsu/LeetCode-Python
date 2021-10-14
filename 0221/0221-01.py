class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        cache = {}
        
        def maxlen(r, c):
            if r >= m or c >= n:
                return 0
            
            if (r, c) not in cache:
                down  = maxlen(r+1, c)
                right = maxlen(r, c+1)
                diag  = maxlen(r+1, c+1)
                
                cache[(r, c)] = 0
                if matrix[r][c] == '1':
                    cache[(r, c)] = 1 + min(down, right, diag)
            
            return cache[(r, c)]
        
        maxlen(0, 0)
        return max(cache.values()) ** 2
