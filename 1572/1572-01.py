class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        l, r = 0, len(mat) - 1

        for row in mat:
            if l == r:
                ans += row[l]
            else:
                ans += row[l]
                ans += row[r]

            l += 1
            r -= 1

        return ans
