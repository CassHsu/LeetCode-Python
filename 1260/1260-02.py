class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        for _ in range(k):
            prev = grid[-1][-1]
            
            for r in range(m):
                for c in range(n):
                    t = grid[r][c]
                    grid[r][c] = prev
                    prev = t
        
        return grid
