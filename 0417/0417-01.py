class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        p_set = set()
        a_set = set()
        
        def dfs(r, c, s):
            s.add((r, c))
            
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + x, c + y
                
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                    
                if (nr, nc) in s:
                    continue
                    
                if heights[nr][nc] < heights[r][c]:
                    continue
                    
                dfs(nr, nc, s)
                
        for i in range(m):
            dfs(i, 0, p_set)
            dfs(i, n - 1, a_set)
            
        for i in range(n):
            dfs(0, i, p_set)
            dfs(m - 1, i, a_set)
            
        return list(p_set.intersection(a_set))
