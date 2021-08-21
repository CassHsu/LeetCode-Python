class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        
        for row in (*grid, *zip(*grid)):
            row = 0, *row, 0
            count += sum([1 if row[i] != row[i - 1] else 0 for i in range(1, len(row))])
        
        return count
