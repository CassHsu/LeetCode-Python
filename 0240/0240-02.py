class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(0, rows):
            if target >= matrix[i][0] and target <= matrix[i][cols-1]:
                low = 0
                high = cols - 1

                while low <= high:
                    mid = (low + high) // 2

                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        high = mid - 1
                    else:
                        low = mid+1

        return False
