class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        step = 0
        res = money

        for p in sorted(prices):
            if p <= res:
                res -= p
                step += 1

                if step == 2:
                    return res
            else:
                return money
        return money
