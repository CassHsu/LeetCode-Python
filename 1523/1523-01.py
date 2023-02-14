class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        
        ans = (high + 1  - low) / 2

        return math.ceil(ans)
