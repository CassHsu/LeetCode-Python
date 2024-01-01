class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        ans = float('inf')
        size = len(prices)

        for i in range(size):
            for j in range(size):
                if i != j:
                    val = prices[i] + prices[j]
                    ans = min(ans, val)

        res = money - ans
        if res >= 0:
            return res

        return money
