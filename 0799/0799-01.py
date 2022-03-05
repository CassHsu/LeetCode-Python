class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        t = [[0] * k for k in range(1, 102)]
        
        t[0][0] = poured
        for row in range(query_row + 1):
            for c in range(row + 1):
                q = (t[row][c] - 1.0) / 2.0
                
                if q > 0:
                    t[row + 1][c] += q
                    t[row + 1][c + 1] += q
                    
        return min(1, t[query_row][query_glass])
