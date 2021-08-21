class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        
        land = 0
        neightbor = 0
        
        for i in range(h):
            for j in range(w):
                c = grid[i][j]
                
                if c == 1:
                    land += 1
                    if i + 1 < h and grid[i + 1][j] == 1:
                        neightbor += 1
                    
                    if j + 1 < w and grid[i][j + 1] == 1:
                        neightbor += 1
        
        return land * 4 - neightbor * 2
