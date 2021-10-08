class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        if r == 0:
            return []
        
        c = len(mat[0])
        d = [[float('inf') for _ in range(c)] for _ in range(r)]
        
        q = collections.deque([])
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    d[i][j] = 0
                    q.append((i, j))
                    
        while len(q) > 0:
            i, j = q.popleft()
            
            for (x, y) in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < r and 0 <= y < c and d[x][y] > d[i][j] + 1:
                    d[x][y] = d[i][j] + 1
                    q.append((x, y))
        
        return d
