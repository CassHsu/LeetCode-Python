class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        MOD = 1_000_000_007
        
        for _ in range(n):
            arr = [0] * (target + 1)
            
            for t in range(target, -1, -1):
                for p in range(1, k + 1):
                    if t >= p:
                        arr[t] += dp[t - p]
                        
                arr[t] %= MOD
            
            dp = arr
        
        return dp[-1]
