class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        cache = {}
        
        for x in reversed(range(0, m)):
            for y in reversed(range(0, n)):
                if x == m-1 and y == n-1:
                    cache[x, y] = max(1, 1 - dungeon[x][y])
                elif x == m-1:
                    cache[x, y] = max(1, cache[x, y+1] - dungeon[x][y])
                elif y == n-1:
                    cache[x, y] = max(1, cache[x+1, y] - dungeon[x][y])
                else:
                    right = cache[x+1, y]
                    down  = cache[x, y+1]
                    
                    if right < down:
                        cache[x, y] = max(1, right - dungeon[x][y])
                    else:
                        cache[x, y] = max(1, down - dungeon[x][y])
        return cache[0, 0]
