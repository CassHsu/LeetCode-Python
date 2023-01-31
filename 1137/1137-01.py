class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1 if i > 2 else i for i in range(n + 1)]
        if len(dp) >= 3:
            dp[2] = 1

        def f(x: int):
            if dp[x] != -1:
                return dp[x]

            dp[x] = f(x - 3) + f(x - 2) + f(x - 1)
            return dp[x]

        f(n)
        return dp[n]
