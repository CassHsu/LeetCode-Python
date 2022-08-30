class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        num = 0
        
        def bfs(r, c):
            if r in range(rows) \
                and c in range(cols) \
                and (r, c) not in visited \
                and grid[r][c] == "1":
                
                grid[r][c] = '0'
                visited.add((r, c))
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    num += 1
            
        return num
