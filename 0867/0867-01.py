class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = [[None] * len(matrix) for _ in range(len(matrix[0]))]
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ret[c][r] = val
                
        return ret
