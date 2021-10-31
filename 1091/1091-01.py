class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        length, queue = len(grid), deque([(0,0,1)])
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

        if grid[0][0] == 1 or grid[length-1][length-1] == 1:
            return -1
        
        grid[0][0] = 1
        
        while queue:
            x, y, dist = queue.popleft()
            
            if (x,y) == (length-1, length-1):
                return dist

            for newX,newY in directions:
                i, j = x + newX, y + newY

                if 0 <= i < length and 0 <= j < length and grid[i][j] == 0:
                    queue.append((i, j, dist+1))
                    grid[i][j] = 1
                    
        return -1
