class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        def map_2d_to_1d(r, c):
            return r * n + c
        
        def map_1d_to_2d(v):
            return [v // n, v % n]
        
        for r in range(m):
            for c in range(n):
                v = map_2d_to_1d(r, c)
                shift = (v + k) % (m * n)
                p = map_1d_to_2d(shift)
                res[p[0]][p[1]] = grid[r][c]
        
        return res
