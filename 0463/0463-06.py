class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        count = 0
        
        for i in range(h):
            for j in range(w):
                c = grid[i][j]
                
                if c == 1:
                    count += 4
                    if i + 1 < h and grid[i + 1][j] == 1:
                        count -= 2
                    
                    if j + 1 < w and grid[i][j + 1] == 1:
                        count -= 2
        
        return count
