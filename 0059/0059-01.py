class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        
        count = 1
        dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        row = 0
        col = 0
        
        while count <= n * n:
            res[row][col] = count
            count += 1
            
            r = floor((row + dr[d][0]) % n)
            c = floor((col + dr[d][1]) % n)
        
            if res[r][c] != 0:
                d = (d + 1) % 4
                
            row += dr[d][0]
            col += dr[d][1]
        
        return res
