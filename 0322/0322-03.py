# Bottom Up 2
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 or len(coins) == 0:
            return 0
        
        cache = [0] + [amount+1] * amount
        
        for c in coins:
            for i in range(c, amount+1):
                cache[i] = min(cache[i - c] + 1, cache[i])
        
        return cache[amount] if cache[amount] < amount + 1 else -1