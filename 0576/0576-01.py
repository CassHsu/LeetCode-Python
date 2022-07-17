class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def dfs(i, j, N, dic):
            if (i, j, N) in dic:
                return dic[(i,j, N)]
        
            if N != 0:
                r = 0
                r += 1 if i - 1  < 0 else dfs(i - 1, j, N - 1, dic)
                r += 1 if i + 1 == m else dfs(i + 1, j, N - 1, dic)
                r += 1 if j - 1  < 0 else dfs(i, j - 1, N - 1, dic)
                r += 1 if j + 1 == n else dfs(i, j + 1, N - 1, dic)
                dic[(i, j, N)] = r
                
                return r
                
            return 0
        
        return dfs(startRow, startColumn, maxMove, {}) % (10 ** 9 + 7)
