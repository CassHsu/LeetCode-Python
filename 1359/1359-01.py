class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 1

        for i in range(1, 2 * n + 1):
            ans = ans * i
            
            if not i % 2:
                ans = ans // 2
            ans %= MOD
        
        return ans
