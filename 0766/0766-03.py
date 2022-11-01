class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        
        for i in range(R):
            for j in range(C):
                if i + 1 < R and j + 1 < C:
                    if matrix[i][j] != matrix[i + 1][j + 1]:
                        return False
        return True
