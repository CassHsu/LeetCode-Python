class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:        
        def check_coast(idx, size, last, curr):
            count = 0
            if last != curr:
                count += 1
                
            if curr == 1 and idx == size - 1:
                count += 1
                
            return count
            
        count = 0
        
        for row in grid:
            for i, curr in enumerate(row):
                last = 0 if i == 0 else row[i - 1]
                count += check_coast(i, len(row), last, curr)
                
        for col in zip(*grid):
            for i, curr in enumerate(col):
                last = 0 if i == 0 else col[i - 1]
                count += check_coast(i, len(col), last, curr)
        
        return count
