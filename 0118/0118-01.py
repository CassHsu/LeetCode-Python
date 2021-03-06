class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            ret.append([1] * (i+1))
            
            for j in range(1, len(ret[i]) - 1):
                ret[i][j] = ret[i-1][j-1] + ret[i-1][j]
        
        return ret
