class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alphablet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        targets = s.split(':')
        res = []
        
        col_start = ord(targets[0][0]) - 65
        col_end = ord(targets[1][0]) - 65
        
        row_start = int(targets[0][1])
        row_end = int(targets[1][1])
        
        for c in range(col_start, col_end + 1):
            for r in range(row_start, row_end + 1):
                res.append(alphablet[c] + str(r))
        
        return res
