class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        islands = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    islands += 1
                    self.dfs(grid, row, col, r, c)
        
        return islands
    
    def dfs(self, grid, row, col, r, c):
        if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0":
            return
        else:
            grid[r][c] = "0"
            self.dfs(grid, row, col, r-1, c)
            self.dfs(grid, row, col, r, c-1)
            self.dfs(grid, row, col, r+1, c)
            self.dfs(grid, row, col, r, c+1)
