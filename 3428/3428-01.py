class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x = 0
        d = [[0] * 100 for _ in range(100)]
        for i in range(n):
            for j in range(n):
                d[i][j] = x
                x += 1

        i, j = 0, 0
        for c in commands:
            if c == "RIGHT":
                j += 1
            elif c == "DOWN":
                i += 1
            elif c == "LEFT":
                j -= 1
            elif c == "UP":
                i -= 1

        return d[i][j]
