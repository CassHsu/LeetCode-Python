class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for n in row:
                if n < 0:
                    count += 1
                    
        return count
