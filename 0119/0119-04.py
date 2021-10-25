class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1]]
        
        for i in range(1, rowIndex+1):
            row = [1 for _ in range(i+1)]
            
            for j in range(1, len(dp[-1])):
                row[j] = dp[-1][j-1] + dp[-1][j]
            
            dp.append(row)
        
        return dp[-1]
