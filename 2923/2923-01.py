class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        ws = [0 for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ws[i] += 1

        champion = (0, 0)
        for i, w in enumerate(ws):
            if w > champion[1]:
                champion = (i, w)

        return champion[0]
