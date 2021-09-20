class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        w = len(matrix[0])
        h = len(matrix)
        
        if target < matrix[0][0]:
            return False
        if target > matrix[h-1][w-1]:
            return False
        
        init = [m[0] for m in matrix]
        idx = 0
        for i in range(h):
            if i == h - 1 and init[i] <= target:
                idx = i
                break
            elif init[i] <= target and target < init[i + 1]:
                idx = i
                break
                
        return target in matrix[idx]
