class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        time = 0
        good = [(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1]
        
        def checkRotten(i, j):
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 2:
                    return True
            return False
        
        while True:
            new_good = []
            new_rotten = []
            for i, j in good:
                if checkRotten(i, j):
                    new_rotten.append((i, j))
                    
                else:
                    new_good.append((i, j))
                    
            if len(new_good) == len(good):
                break
                
            else:
                time += 1
                good = new_good
                
                for i, j in new_rotten:
                    grid[i][j] = 2
                    
        return -1 if good else time
