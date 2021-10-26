class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        dp = [math.inf] * (n+1)
        dp[n] = 0

        for i in reversed(range(n)):
            t = intervals[i][1]
            l, r = i+1, n

            while l < r:
                m = (l+r) // 2
                if intervals[m][0] < t:
                    l = m+1
                else:
                    r = m

            dp[i] = min(dp[i+1]+1, dp[l]+(l-i-1))

        return dp[0]
