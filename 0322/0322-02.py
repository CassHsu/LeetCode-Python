# Top-Down
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(rest):
            if rest < 0:
                return amount + 1
            if rest == 0:
                return 0
                        
            if rest not in cache:
                cache[rest] = 1+min([dfs(rest-c) for c in coins])
            
            return cache[rest]
        
        cache = {}
        res = dfs(amount)
        
        return res if res < amount + 1 else -1