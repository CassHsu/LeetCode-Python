class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = 0
        cash = 0
        hold = float('-inf')
        
        for p in prices:
            prev, cash, hold = cash, max(cash, hold + p), max(hold, prev - p)
            
        return cash
