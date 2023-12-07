class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        d = 0
        r = 0

        while d < n:
            if d % 7 == 0:
                r = d // 7 + 1
            else:
                r += 1

            money += r
            d += 1

        return money
