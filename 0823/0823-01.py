class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        arr.sort()
        dp = [1] * n
        idx = { a: i for i, a in enumerate(arr) }
        
        for i, a in enumerate(arr):
            for j in range(i):
                if a % arr[j] == 0:
                    r = a / arr[j]
                    
                    if r in idx:
                        dp[i] += dp[j] * dp[idx[r]]
                        dp[i] %= mod
        
        return sum(dp) % mod
