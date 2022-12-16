class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort(reverse=True)

        ans = 0
        for i in range(len(grid[0])):
            mx = 0

            for j in range(len(grid)):
                mx = max(grid[j][i], mx)

            ans += mx

        return ans
