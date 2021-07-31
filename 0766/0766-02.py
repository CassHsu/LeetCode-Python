class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ret = [r == 0 or c == 0 or matrix[r - 1][c - 1] == v for r, row in enumerate(matrix) for c, v in enumerate(row)]
        return all(ret)
