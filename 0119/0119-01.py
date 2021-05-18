class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = []
        
        for i in range(rowIndex+1):
            ret.append([1] * (i+1))
            
            for j in range(1, len(ret[i]) - 1):
                ret[i][j] = ret[i-1][j-1] + ret[i-1][j]
                
        return ret[-1]
