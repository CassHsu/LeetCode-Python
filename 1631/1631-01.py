class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        res = 0
        heap = [(0, 0, 0)]
        
        while heap:
            diff, x, y = heappop(heap)
            res = max(res, diff)
            
            if x == m - 1 and y == n - 1:
                return res
            
            if heights[x][y] == 0:
                continue
                
            curr_h = heights[x][y]
            heights[x][y] = 0
            
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] != 0:
                    nd = abs(heights[nx][ny] - curr_h)
                    heappush(heap, (nd, nx, ny))
                    
        return res
