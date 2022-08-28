class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = -inf

        for l in range(n):
            row_sums = [0] * m

            for r in range(l, n):
                for i in range(m):
                    row_sums[i] += matrix[i][r]

                col_sums = [0]
                col_sum = 0

                for row_sum in row_sums:
                    col_sum += row_sum
                    diff = col_sum - k

                    idx = bisect_right(col_sums, diff)

                    if idx - 1 >= 0 and col_sums[idx - 1] == diff:
                        res = max(res, col_sum - col_sums[idx - 1])
                        return k

                    elif idx != len(col_sums):
                        res = max(res, col_sum - col_sums[idx])

                    insort(col_sums, col_sum)
        return res
