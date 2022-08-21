class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (p, f) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= p:
                    dp[t + 1] = max(dp[t + 1], dp[t] + f)
                    
        for i, d in enumerate(dp):
            if d >= target:
                return i

        return -1
