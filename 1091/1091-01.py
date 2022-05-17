class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, q = len(grid), deque([(0,0,1)])
        d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        grid[0][0] = 1
        
        while q:
            x, y, dist = q.popleft()
            
            if (x,y) == (n - 1, n-1):
                return dist

            for nx, ny in d:
                i, j = x + nx, y + ny

                if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                    q.append((i, j, dist + 1))
                    grid[i][j] = 1
                    
        return -1
