class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        
        for row in grid:
            row = 0, *row, 0
            for i in range(1, len(row)):
                if row[i] != row[i - 1]:
                    count += 1
                    
        for col in zip(*grid):
            col = 0, *col, 0
            for i in range(1, len(col)):
                if col[i] != col[i - 1]:
                    count += 1
        
        return count
