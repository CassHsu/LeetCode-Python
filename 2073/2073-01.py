class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:        
        ans = 0
        count = tickets[k]
        n = len(tickets)
        
        for r in range(count):
            for c in range(n):
                if r == count - 1 and c > k:
                    break
                
                if tickets[c] > 0:
                    tickets[c] -= 1
                    ans += 1
        
        return ans
