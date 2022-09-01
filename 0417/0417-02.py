class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        p_set = set()
        a_set = set()
        
        def dfs(r, c, s, prev_h):
            if (r, c) in s or r < 0 or c < 0 or r == m or c == n or heights[r][c] < prev_h:
                return
            
            s.add((r, c))
            dfs(r + 1, c, s, heights[r][c])
            dfs(r - 1, c, s, heights[r][c])
            dfs(r, c + 1, s, heights[r][c])
            dfs(r, c - 1, s, heights[r][c])
            
        for r in range(m):
            dfs(r, 0, p_set, heights[r][0])
            dfs(r, n - 1, a_set, heights[r][n - 1])
            
        for c in range(n):
            dfs(0, c, p_set, heights[0][c])
            dfs(m - 1, c, a_set, heights[m - 1][c])
            
        return list(p_set.intersection(a_set))
