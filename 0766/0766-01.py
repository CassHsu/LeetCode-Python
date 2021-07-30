class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = {}
        for r, row in enumerate(matrix):
            for c, v in enumerate(row):
                if r - c not in m:
                    m[r - c] = v
                elif m[r - c] != v:
                    return False
        return True
