class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(0, cols):
            if target >= matrix[0][i] and target <= matrix[rows-1][i]:
                low = 0
                high = rows - 1

                while low <= high:
                    mid = (low + high) // 2

                    if matrix[mid][i] == target:
                        return True
                    elif matrix[mid][i] > target:
                        high = mid-1
                    else:
                        low = mid+1

        return False
