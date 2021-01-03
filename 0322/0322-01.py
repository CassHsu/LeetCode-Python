# Bottom up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [0] + [amount+1] * amount
        
        for i in range(amount + 1):
            for c in coins:
                if i - c < 0:
                    continue
                
                cache[i] = min(cache[i - c] + 1, cache[i])
                
        return cache[amount] if cache[amount] < amount + 1 else -1