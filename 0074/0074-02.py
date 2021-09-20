class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        w = len(matrix[0])
        h = len(matrix)
        
        if target < matrix[0][0]:
            return False
        if target > matrix[h-1][w-1]:
            return False
        
        def check(nums):            
            if target in nums:
                return True
            else:
                return False
        
        for m in matrix:
            if check(m):
                return True
        
        return False
