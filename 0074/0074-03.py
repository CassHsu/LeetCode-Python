class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        full = []
        
        for row in matrix:
            full += row
            
        start = 0
        end = len(full) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            if full[mid] > target:
                end = mid - 1
            elif full[mid] < target:
                start = mid + 1
            else:
                return True
            
        return False
