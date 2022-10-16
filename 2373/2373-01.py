class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        for r in range(0, len(grid) - 2):
            mx = []
            for c in range(0, len(grid[0]) - 2):
                v1 = max(grid[r][c], grid[r][c + 1], grid[r][c + 2])
                v2 = max(grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2])
                v3 = max(grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2])
                mx.append(max(v1, v2, v3))
            
            res.append(mx)
        
        return res
